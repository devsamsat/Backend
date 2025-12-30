from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends, HTTPException, Request, status
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.infrastructure.orm.table_registry import get_table
from app.infrastructure.repositories.table_repository_impl import TableRepositoryImpl
from app.schemas.table_schema import (
    TableRecordCreate,
    TableRecordResponse,
    TableRecordUpdate,
)
from app.usecases.table_usecase import TableUseCase


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_usecase(db: Session = Depends(get_db)) -> TableUseCase:
    repo = TableRepositoryImpl(db)
    return TableUseCase(repo)


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

    router = APIRouter(prefix=f"/api/v1/{table_name}", tags=[table_name])

    @router.get("/", response_model=list[TableRecordResponse])
    def list_records(uc: TableUseCase = Depends(get_usecase)):
        return uc.get_all(table_name)

    @router.post("/", response_model=TableRecordResponse)
    def create_record(
        payload: TableRecordCreate,
        uc: TableUseCase = Depends(get_usecase),
    ):
        return uc.create(table_name, payload.data)

    if len(pk_columns) == 1:
        pk_name = pk_columns[0]

        @router.get("/{pk_value}", response_model=TableRecordResponse)
        def get_record(pk_value: str, uc: TableUseCase = Depends(get_usecase)):
            record = uc.get_by_id(table_name, {pk_name: pk_value})
            if not record:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"{table_name} record not found",
                )
            return record

        @router.put("/{pk_value}", response_model=TableRecordResponse)
        def update_record(
            pk_value: str,
            payload: TableRecordUpdate,
            uc: TableUseCase = Depends(get_usecase),
        ):
            record = uc.update(table_name, {pk_name: pk_value}, payload.data)
            if not record:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"{table_name} record not found",
                )
            return record

        @router.delete("/{pk_value}")
        def delete_record(pk_value: str, uc: TableUseCase = Depends(get_usecase)):
            deleted = uc.delete(table_name, {pk_name: pk_value})
            if not deleted:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"{table_name} record not found",
                )
            return {"message": "Deleted"}
    else:

        @router.get("/by-key", response_model=TableRecordResponse)
        def get_record_by_key(
            request: Request,
            uc: TableUseCase = Depends(get_usecase),
        ):
            pk_values = _extract_pk_values(table_name, request)
            record = uc.get_by_id(table_name, pk_values)
            if not record:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"{table_name} record not found",
                )
            return record

        @router.put("/by-key", response_model=TableRecordResponse)
        def update_record_by_key(
            request: Request,
            payload: TableRecordUpdate,
            uc: TableUseCase = Depends(get_usecase),
        ):
            pk_values = _extract_pk_values(table_name, request)
            record = uc.update(table_name, pk_values, payload.data)
            if not record:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"{table_name} record not found",
                )
            return record

        @router.delete("/by-key")
        def delete_record_by_key(
            request: Request,
            uc: TableUseCase = Depends(get_usecase),
        ):
            pk_values = _extract_pk_values(table_name, request)
            deleted = uc.delete(table_name, pk_values)
            if not deleted:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"{table_name} record not found",
                )
            return {"message": "Deleted"}

    return router
