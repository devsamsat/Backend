from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.infrastructure.repositories.jnsumum_repository_impl import JnsUmumRepositoryImpl
from app.schemas.jnsumum_schema import (
    JnsUmumCreate,
    JnsUmumResponse,
    JnsUmumUpdate,
)
from app.usecases.jnsumum_usecase import JnsUmumUseCase

router = APIRouter(prefix="/api/v1/jnsumum", tags=["jnsumum"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_usecase(db: Session = Depends(get_db)):
    repo = JnsUmumRepositoryImpl(db)
    return JnsUmumUseCase(repo)


@router.post("/", response_model=JnsUmumResponse)
def create_jnsumum(
    payload: JnsUmumCreate,
    uc: JnsUmumUseCase = Depends(get_usecase),
):
    return uc.create(
        payload.kdumum,
        payload.nmumum,
        payload.keterangan,
        payload.status,
        payload.created_by,
        payload.updated_by,
    )


@router.get("/", response_model=list[JnsUmumResponse])
def get_jnsumums(uc: JnsUmumUseCase = Depends(get_usecase)):
    return uc.get_all()


@router.get("/{kdumum}", response_model=JnsUmumResponse)
def get_jnsumum(kdumum: str, uc: JnsUmumUseCase = Depends(get_usecase)):
    record = uc.get_by_id(kdumum)
    if not record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="JnsUmum not found",
        )
    return record


@router.put("/{kdumum}", response_model=JnsUmumResponse)
def update_jnsumum(
    kdumum: str,
    payload: JnsUmumUpdate,
    uc: JnsUmumUseCase = Depends(get_usecase),
):
    record = uc.update(
        kdumum,
        payload.nmumum,
        payload.keterangan,
        payload.status,
        payload.updated_by,
    )
    if not record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="JnsUmum not found",
        )
    return record


@router.delete("/{kdumum}")
def delete_jnsumum(kdumum: str, uc: JnsUmumUseCase = Depends(get_usecase)):
    deleted = uc.delete(kdumum)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="JnsUmum not found",
        )
    return {"message": "Deleted"}
