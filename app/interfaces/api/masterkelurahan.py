from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.infrastructure.repositories.masterkelurahan_repository_impl import (
    MasterKelurahanRepositoryImpl,
)
from app.usecases.masterkelurahan_usecase import MasterKelurahanUseCase
from app.schemas.masterkelurahan_schema import (
    MasterKelurahanCreate,
    MasterKelurahanResponse,
    MasterKelurahanUpdate,
)

router = APIRouter(prefix="/api/v1/masterkelurahan", tags=["masterkelurahan"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_usecase(db: Session = Depends(get_db)):
    repo = MasterKelurahanRepositoryImpl(db)
    return MasterKelurahanUseCase(repo)


@router.post("/", response_model=MasterKelurahanResponse)
def create_masterkelurahan(
    payload: MasterKelurahanCreate,
    uc: MasterKelurahanUseCase = Depends(get_usecase),
):
    return uc.create(
        payload.idkecamatan,
        payload.nmkelurahan,
        payload.alamat,
        payload.telepon,
        payload.status,
        payload.kdkelurahan,
        payload.kodepos,
        payload.created_by,
        payload.updated_by,
    )


@router.get("/", response_model=list[MasterKelurahanResponse])
def get_masterkelurahans(uc: MasterKelurahanUseCase = Depends(get_usecase)):
    return uc.get_all()


@router.get("/{idkelurahan}", response_model=MasterKelurahanResponse)
def get_masterkelurahan(
    idkelurahan: int,
    uc: MasterKelurahanUseCase = Depends(get_usecase),
):
    master_kelurahan = uc.get_by_id(idkelurahan)
    if not master_kelurahan:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MasterKelurahan not found",
        )
    return master_kelurahan


@router.put("/{idkelurahan}", response_model=MasterKelurahanResponse)
def update_masterkelurahan(
    idkelurahan: int,
    payload: MasterKelurahanUpdate,
    uc: MasterKelurahanUseCase = Depends(get_usecase),
):
    master_kelurahan = uc.update(
        idkelurahan,
        payload.idkecamatan,
        payload.nmkelurahan,
        payload.alamat,
        payload.telepon,
        payload.status,
        payload.kdkelurahan,
        payload.kodepos,
        payload.updated_by,
    )
    if not master_kelurahan:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MasterKelurahan not found",
        )
    return master_kelurahan


@router.delete("/{idkelurahan}")
def delete_masterkelurahan(
    idkelurahan: int,
    uc: MasterKelurahanUseCase = Depends(get_usecase),
):
    deleted = uc.delete(idkelurahan)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MasterKelurahan not found",
        )
    return {"message": "Deleted"}
