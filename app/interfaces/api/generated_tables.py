from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends, HTTPException, Request, status
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.core.table_constants import CUSTOM_TABLES
from app.domain.entities.generated_entities import ENTITY_REGISTRY
from app.infrastructure.orm.table_registry import TABLE_NAMES, get_table
from app.infrastructure.repositories.generated_table_repository_impl import get_repository_class
from app.schemas.generated_table_schemas import SCHEMA_REGISTRY
from app.usecases.generated_table_usecases import get_usecase_class


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def _extract_pk_values(table_name: str, request: Request) -> dict[str, Any]:
    table = get_table(table_name)
    pk_columns = [col.name for col in table.primary_key.columns]
    missing = [col for col in pk_columns if col not in request.query_params]
    if missing:
        missing_cols = ", ".join(missing)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Missing primary key values: {missing_cols}",
        )
    return {col: request.query_params[col] for col in pk_columns}


def create_table_router(table_name: str) -> APIRouter:
    table = get_table(table_name)
    pk_columns = [col.name for col in table.primary_key.columns]
    schemas = SCHEMA_REGISTRY[table_name]
    entity_cls = ENTITY_REGISTRY[table_name]
    repo_cls = get_repository_class(table_name)
    usecase_cls = get_usecase_class(table_name)

    router = APIRouter(prefix=f"/api/v1/{table_name}", tags=[table_name])

    def get_usecase(db: Session = Depends(get_db)):
        return usecase_cls(repo_cls(db))

    @router.get("/", response_model=list[schemas.response])
    def list_records(uc=Depends(get_usecase)):
        return uc.get_all()

    @router.post("/", response_model=schemas.response)
    def create_record(payload: schemas.create, uc=Depends(get_usecase)):
        data = payload.model_dump(exclude_unset=True)
        entity = entity_cls(**data)
        return uc.create(entity)

    if len(pk_columns) == 1:
        pk_name = pk_columns[0]

        @router.get("/{pk_value}", response_model=schemas.response)
        def get_record(pk_value: str, uc=Depends(get_usecase)):
            record = uc.get_by_id({pk_name: pk_value})
            if not record:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"{table_name} record not found",
                )
            return record

        @router.put("/{pk_value}", response_model=schemas.response)
        def update_record(pk_value: str, payload: schemas.update, uc=Depends(get_usecase)):
            data = payload.model_dump(exclude_unset=True)
            entity = entity_cls(**data)
            record = uc.update({pk_name: pk_value}, entity)
            if not record:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"{table_name} record not found",
                )
            return record

        @router.delete("/{pk_value}")
        def delete_record(pk_value: str, uc=Depends(get_usecase)):
            deleted = uc.delete({pk_name: pk_value})
            if not deleted:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"{table_name} record not found",
                )
            return {"message": "Deleted"}
    else:

        @router.get("/by-key", response_model=schemas.response)
        def get_record_by_key(request: Request, uc=Depends(get_usecase)):
            pk_values = _extract_pk_values(table_name, request)
            record = uc.get_by_id(pk_values)
            if not record:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"{table_name} record not found",
                )
            return record

        @router.put("/by-key", response_model=schemas.response)
        def update_record_by_key(
            request: Request,
            payload: schemas.update,
            uc=Depends(get_usecase),
        ):
            pk_values = _extract_pk_values(table_name, request)
            data = payload.model_dump(exclude_unset=True)
            entity = entity_cls(**data)
            record = uc.update(pk_values, entity)
            if not record:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"{table_name} record not found",
                )
            return record

        @router.delete("/by-key")
        def delete_record_by_key(request: Request, uc=Depends(get_usecase)):
            pk_values = _extract_pk_values(table_name, request)
            deleted = uc.delete(pk_values)
            if not deleted:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"{table_name} record not found",
                )
            return {"message": "Deleted"}

    return router


def generate_table_routers() -> list[APIRouter]:
    routers = []
    for table_name in TABLE_NAMES:
        if table_name in CUSTOM_TABLES:
            continue
        routers.append(create_table_router(table_name))
    return routers
