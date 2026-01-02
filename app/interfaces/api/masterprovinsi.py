from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.infrastructure.repositories.masterprovinsi_repository_impl import (
    MasterProvinsiRepositoryImpl,
)
from app.usecases.masterprovinsi_usecase import MasterProvinsiUseCase
from app.schemas.masterprovinsi_schema import (
    MasterProvinsiCreate,
    MasterProvinsiResponse,
    MasterProvinsiUpdate,
)

router = APIRouter(prefix="/api/v1/masterprovinsi", tags=["masterprovinsi"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_usecase(db: Session = Depends(get_db)):
    repo = MasterProvinsiRepositoryImpl(db)
    return MasterProvinsiUseCase(repo)


@router.post("/", response_model=MasterProvinsiResponse)
def create_masterprovinsi(
    payload: MasterProvinsiCreate,
    uc: MasterProvinsiUseCase = Depends(get_usecase),
):
    return uc.create(
        payload.kdprovinsi,
        payload.nmprovinsi,
        payload.status,
        payload.created_by,
        payload.updated_by,
    )


@router.get("/", response_model=list[MasterProvinsiResponse])
def get_masterprovinsis(uc: MasterProvinsiUseCase = Depends(get_usecase)):
    return uc.get_all()


@router.get("/{idprovinsi}", response_model=MasterProvinsiResponse)
def get_masterprovinsi(idprovinsi: int, uc: MasterProvinsiUseCase = Depends(get_usecase)):
    master_provinsi = uc.get_by_id(idprovinsi)
    if not master_provinsi:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MasterProvinsi not found",
        )
    return master_provinsi


@router.put("/{idprovinsi}", response_model=MasterProvinsiResponse)
def update_masterprovinsi(
    idprovinsi: int,
    payload: MasterProvinsiUpdate,
    uc: MasterProvinsiUseCase = Depends(get_usecase),
):
    master_provinsi = uc.update(
        idprovinsi,
        payload.kdprovinsi,
        payload.nmprovinsi,
        payload.status,
        payload.updated_by,
    )
    if not master_provinsi:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MasterProvinsi not found",
        )
    return master_provinsi


@router.delete("/{idprovinsi}")
def delete_masterprovinsi(
    idprovinsi: int,
    uc: MasterProvinsiUseCase = Depends(get_usecase),
):
    deleted = uc.delete(idprovinsi)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MasterProvinsi not found",
        )
    return {"message": "Deleted"}
