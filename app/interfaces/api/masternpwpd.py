from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.infrastructure.repositories.masternpwpd_repository_impl import MasterNpwpdRepositoryImpl
from app.schemas.masternpwpd_schema import (
    MasterNpwpdCreate,
    MasterNpwpdResponse,
    MasterNpwpdUpdate,
)
from app.usecases.masternpwpd_usecase import MasterNpwpdUseCase

router = APIRouter(prefix="/api/v1/masternpwpd", tags=["masternpwpd"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_usecase(db: Session = Depends(get_db)):
    repo = MasterNpwpdRepositoryImpl(db)
    return MasterNpwpdUseCase(repo)


@router.post("/", response_model=MasterNpwpdResponse)
def create_masternpwpd(
    payload: MasterNpwpdCreate,
    uc: MasterNpwpdUseCase = Depends(get_usecase),
):
    return uc.create(
        payload.statnpwpd,
        payload.npwpd,
        payload.idbadan,
        payload.idktp,
        payload.tgldaftar,
        payload.nib,
        payload.namabadan,
        payload.alamat,
        payload.status,
        payload.ket,
        payload.created_by,
        payload.updated_by,
    )


@router.get("/", response_model=list[MasterNpwpdResponse])
def get_masternpwpds(uc: MasterNpwpdUseCase = Depends(get_usecase)):
    return uc.get_all()


@router.get("/{idnpwpd}", response_model=MasterNpwpdResponse)
def get_masternpwpd(idnpwpd: int, uc: MasterNpwpdUseCase = Depends(get_usecase)):
    record = uc.get_by_id(idnpwpd)
    if not record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MasterNpwpd not found",
        )
    return record


@router.put("/{idnpwpd}", response_model=MasterNpwpdResponse)
def update_masternpwpd(
    idnpwpd: int,
    payload: MasterNpwpdUpdate,
    uc: MasterNpwpdUseCase = Depends(get_usecase),
):
    record = uc.update(
        idnpwpd,
        payload.statnpwpd,
        payload.npwpd,
        payload.idbadan,
        payload.idktp,
        payload.tgldaftar,
        payload.nib,
        payload.namabadan,
        payload.alamat,
        payload.status,
        payload.ket,
        payload.updated_by,
    )
    if not record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MasterNpwpd not found",
        )
    return record


@router.delete("/{idnpwpd}")
def delete_masternpwpd(idnpwpd: int, uc: MasterNpwpdUseCase = Depends(get_usecase)):
    deleted = uc.delete(idnpwpd)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MasterNpwpd not found",
        )
    return {"message": "Deleted"}
