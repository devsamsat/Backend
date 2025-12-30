from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.infrastructure.repositories.masterbadan_repository_impl import MasterBadanRepositoryImpl
from app.usecases.masterbadan_usecase import MasterBadanUseCase
from app.schemas.masterbadan_schema import (
    MasterBadanCreate,
    MasterBadanResponse,
    MasterBadanUpdate,
)

router = APIRouter(prefix="/api/v1/masterbadan", tags=["masterbadan"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_usecase(db: Session = Depends(get_db)):
    repo = MasterBadanRepositoryImpl(db)
    return MasterBadanUseCase(repo)


@router.post("/", response_model=MasterBadanResponse)
def create_masterbadan(
    payload: MasterBadanCreate,
    uc: MasterBadanUseCase = Depends(get_usecase),
):
    return uc.create(
        payload.namabadan,
        payload.nohp,
        payload.alamat,
        payload.nib,
        payload.idktp,
        payload.tgldaftar,
        payload.idprovinsi,
        payload.idkabkokta,
        payload.ket,
        payload.created_by,
        payload.updated_by,
    )


@router.get("/", response_model=list[MasterBadanResponse])
def get_masterbadans(uc: MasterBadanUseCase = Depends(get_usecase)):
    return uc.get_all()


@router.get("/{idbadan}", response_model=MasterBadanResponse)
def get_masterbadan(idbadan: int, uc: MasterBadanUseCase = Depends(get_usecase)):
    master_badan = uc.get_by_id(idbadan)
    if not master_badan:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MasterBadan not found",
        )
    return master_badan


@router.put("/{idbadan}", response_model=MasterBadanResponse)
def update_masterbadan(
    idbadan: int,
    payload: MasterBadanUpdate,
    uc: MasterBadanUseCase = Depends(get_usecase),
):
    master_badan = uc.update(
        idbadan,
        payload.namabadan,
        payload.nohp,
        payload.alamat,
        payload.nib,
        payload.idktp,
        payload.tgldaftar,
        payload.idprovinsi,
        payload.idkabkokta,
        payload.ket,
        payload.updated_by,
    )
    if not master_badan:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MasterBadan not found",
        )
    return master_badan


@router.delete("/{idbadan}")
def delete_masterbadan(idbadan: int, uc: MasterBadanUseCase = Depends(get_usecase)):
    deleted = uc.delete(idbadan)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MasterBadan not found",
        )
    return {"message": "Deleted"}
