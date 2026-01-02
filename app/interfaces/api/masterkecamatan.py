from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.infrastructure.repositories.masterkecamatan_repository_impl import (
    MasterKecamatanRepositoryImpl,
)
from app.usecases.masterkecamatan_usecase import MasterKecamatanUseCase
from app.schemas.masterkecamatan_schema import (
    MasterKecamatanCreate,
    MasterKecamatanResponse,
    MasterKecamatanUpdate,
)

router = APIRouter(prefix="/api/v1/masterkecamatan", tags=["masterkecamatan"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_usecase(db: Session = Depends(get_db)):
    repo = MasterKecamatanRepositoryImpl(db)
    return MasterKecamatanUseCase(repo)


@router.post("/", response_model=MasterKecamatanResponse)
def create_masterkecamatan(
    payload: MasterKecamatanCreate,
    uc: MasterKecamatanUseCase = Depends(get_usecase),
):
    return uc.create(
        payload.idkabkota,
        payload.nmkecamatan,
        payload.alamat,
        payload.telepon,
        payload.status,
        payload.kdkecamatan,
        payload.fax,
        payload.created_by,
        payload.updated_by,
    )


@router.get("/", response_model=list[MasterKecamatanResponse])
def get_masterkecamatans(uc: MasterKecamatanUseCase = Depends(get_usecase)):
    return uc.get_all()


@router.get("/{idkecamatan}", response_model=MasterKecamatanResponse)
def get_masterkecamatan(
    idkecamatan: int,
    uc: MasterKecamatanUseCase = Depends(get_usecase),
):
    master_kecamatan = uc.get_by_id(idkecamatan)
    if not master_kecamatan:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MasterKecamatan not found",
        )
    return master_kecamatan


@router.put("/{idkecamatan}", response_model=MasterKecamatanResponse)
def update_masterkecamatan(
    idkecamatan: int,
    payload: MasterKecamatanUpdate,
    uc: MasterKecamatanUseCase = Depends(get_usecase),
):
    master_kecamatan = uc.update(
        idkecamatan,
        payload.idkabkota,
        payload.nmkecamatan,
        payload.alamat,
        payload.telepon,
        payload.status,
        payload.kdkecamatan,
        payload.fax,
        payload.updated_by,
    )
    if not master_kecamatan:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MasterKecamatan not found",
        )
    return master_kecamatan


@router.delete("/{idkecamatan}")
def delete_masterkecamatan(
    idkecamatan: int,
    uc: MasterKecamatanUseCase = Depends(get_usecase),
):
    deleted = uc.delete(idkecamatan)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MasterKecamatan not found",
        )
    return {"message": "Deleted"}
