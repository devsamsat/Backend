from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.infrastructure.repositories.masterpegawai_repository_impl import MasterPegawaiRepositoryImpl
from app.schemas.masterpegawai_schema import (
    MasterPegawaiCreate,
    MasterPegawaiResponse,
    MasterPegawaiUpdate,
)
from app.usecases.masterpegawai_usecase import MasterPegawaiUseCase

router = APIRouter(prefix="/api/v1/masterpegawai", tags=["masterpegawai"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_usecase(db: Session = Depends(get_db)):
    repo = MasterPegawaiRepositoryImpl(db)
    return MasterPegawaiUseCase(repo)


@router.post("/", response_model=MasterPegawaiResponse)
def create_masterpegawai(
    payload: MasterPegawaiCreate,
    uc: MasterPegawaiUseCase = Depends(get_usecase),
):
    return uc.create(
        payload.idktp,
        payload.nip,
        payload.nik,
        payload.nama,
        payload.idupt,
        payload.status,
        payload.jabatan,
        payload.pangkat,
        payload.golongan,
        payload.uid,
        payload.telepon,
        payload.created_by,
        payload.updated_by,
    )


@router.get("/", response_model=list[MasterPegawaiResponse])
def get_masterpegawais(uc: MasterPegawaiUseCase = Depends(get_usecase)):
    return uc.get_all()


@router.get("/{idpegawai}", response_model=MasterPegawaiResponse)
def get_masterpegawai(idpegawai: int, uc: MasterPegawaiUseCase = Depends(get_usecase)):
    record = uc.get_by_id(idpegawai)
    if not record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MasterPegawai not found",
        )
    return record


@router.put("/{idpegawai}", response_model=MasterPegawaiResponse)
def update_masterpegawai(
    idpegawai: int,
    payload: MasterPegawaiUpdate,
    uc: MasterPegawaiUseCase = Depends(get_usecase),
):
    record = uc.update(
        idpegawai,
        payload.idktp,
        payload.nip,
        payload.nik,
        payload.nama,
        payload.idupt,
        payload.status,
        payload.jabatan,
        payload.pangkat,
        payload.golongan,
        payload.uid,
        payload.telepon,
        payload.updated_by,
    )
    if not record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MasterPegawai not found",
        )
    return record


@router.delete("/{idpegawai}")
def delete_masterpegawai(idpegawai: int, uc: MasterPegawaiUseCase = Depends(get_usecase)):
    deleted = uc.delete(idpegawai)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MasterPegawai not found",
        )
    return {"message": "Deleted"}
