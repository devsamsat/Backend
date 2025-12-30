from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.infrastructure.repositories.masterhapusdenda_repository_impl import (
    MasterHapusDendaRepositoryImpl,
)
from app.usecases.masterhapusdenda_usecase import MasterHapusDendaUseCase
from app.schemas.masterhapusdenda_schema import (
    MasterHapusDendaCreate,
    MasterHapusDendaResponse,
    MasterHapusDendaUpdate,
)

router = APIRouter(prefix="/api/v1/masterhapusdenda", tags=["masterhapusdenda"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_usecase(db: Session = Depends(get_db)):
    repo = MasterHapusDendaRepositoryImpl(db)
    return MasterHapusDendaUseCase(repo)


@router.post("/", response_model=MasterHapusDendaResponse)
def create_masterhapusdenda(
    payload: MasterHapusDendaCreate,
    uc: MasterHapusDendaUseCase = Depends(get_usecase),
):
    return uc.create(
        payload.jenis,
        payload.uraian,
        payload.awal,
        payload.akhir,
        payload.nilai,
        payload.satuan,
        payload.ket,
        payload.status,
        payload.created_by,
        payload.updated_by,
    )


@router.get("/", response_model=list[MasterHapusDendaResponse])
def get_masterhapusdendas(uc: MasterHapusDendaUseCase = Depends(get_usecase)):
    return uc.get_all()


@router.get("/{idhapusdenda}", response_model=MasterHapusDendaResponse)
def get_masterhapusdenda(
    idhapusdenda: int,
    uc: MasterHapusDendaUseCase = Depends(get_usecase),
):
    master_hapus_denda = uc.get_by_id(idhapusdenda)
    if not master_hapus_denda:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MasterHapusDenda not found",
        )
    return master_hapus_denda


@router.put("/{idhapusdenda}", response_model=MasterHapusDendaResponse)
def update_masterhapusdenda(
    idhapusdenda: int,
    payload: MasterHapusDendaUpdate,
    uc: MasterHapusDendaUseCase = Depends(get_usecase),
):
    master_hapus_denda = uc.update(
        idhapusdenda,
        payload.jenis,
        payload.uraian,
        payload.awal,
        payload.akhir,
        payload.nilai,
        payload.satuan,
        payload.ket,
        payload.status,
        payload.updated_by,
    )
    if not master_hapus_denda:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MasterHapusDenda not found",
        )
    return master_hapus_denda


@router.delete("/{idhapusdenda}")
def delete_masterhapusdenda(
    idhapusdenda: int,
    uc: MasterHapusDendaUseCase = Depends(get_usecase),
):
    deleted = uc.delete(idhapusdenda)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MasterHapusDenda not found",
        )
    return {"message": "Deleted"}
