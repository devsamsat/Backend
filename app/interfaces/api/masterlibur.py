from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.infrastructure.repositories.masterlibur_repository_impl import MasterLiburRepositoryImpl
from app.schemas.masterlibur_schema import (
    MasterLiburCreate,
    MasterLiburResponse,
    MasterLiburUpdate,
)
from app.usecases.masterlibur_usecase import MasterLiburUseCase

router = APIRouter(prefix="/api/v1/masterlibur", tags=["masterlibur"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_usecase(db: Session = Depends(get_db)):
    repo = MasterLiburRepositoryImpl(db)
    return MasterLiburUseCase(repo)


@router.post("/", response_model=MasterLiburResponse)
def create_masterlibur(
    payload: MasterLiburCreate,
    uc: MasterLiburUseCase = Depends(get_usecase),
):
    return uc.create(
        payload.idkabkota,
        payload.level,
        payload.tanggal,
        payload.namalibur,
        payload.keterangan,
        payload.created_by,
        payload.updated_by,
    )


@router.get("/", response_model=list[MasterLiburResponse])
def get_masterliburs(uc: MasterLiburUseCase = Depends(get_usecase)):
    return uc.get_all()


@router.get("/{idlibur}", response_model=MasterLiburResponse)
def get_masterlibur(idlibur: int, uc: MasterLiburUseCase = Depends(get_usecase)):
    record = uc.get_by_id(idlibur)
    if not record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MasterLibur not found",
        )
    return record


@router.put("/{idlibur}", response_model=MasterLiburResponse)
def update_masterlibur(
    idlibur: int,
    payload: MasterLiburUpdate,
    uc: MasterLiburUseCase = Depends(get_usecase),
):
    record = uc.update(
        idlibur,
        payload.idkabkota,
        payload.level,
        payload.tanggal,
        payload.namalibur,
        payload.keterangan,
        payload.updated_by,
    )
    if not record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MasterLibur not found",
        )
    return record


@router.delete("/{idlibur}")
def delete_masterlibur(idlibur: int, uc: MasterLiburUseCase = Depends(get_usecase)):
    deleted = uc.delete(idlibur)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MasterLibur not found",
        )
    return {"message": "Deleted"}
