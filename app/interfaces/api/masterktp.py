from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.infrastructure.repositories.masterktp_repository_impl import MasterKtpRepositoryImpl
from app.usecases.masterktp_usecase import MasterKtpUseCase
from app.schemas.masterktp_schema import (
    MasterKtpCreate,
    MasterKtpResponse,
    MasterKtpUpdate,
)

router = APIRouter(prefix="/api/v1/masterktp", tags=["masterktp"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_usecase(db: Session = Depends(get_db)):
    repo = MasterKtpRepositoryImpl(db)
    return MasterKtpUseCase(repo)


@router.post("/", response_model=MasterKtpResponse)
def create_masterktp(
    payload: MasterKtpCreate,
    uc: MasterKtpUseCase = Depends(get_usecase),
):
    return uc.create(
        payload.nik,
        payload.nama,
        payload.nohp,
        payload.alamat,
        payload.idkabkokta,
        payload.idkecamatan,
        payload.idkelurahan,
        payload.agama,
        payload.tgldaftar,
        payload.idprovinsi,
        payload.idrw,
        payload.idrt,
        payload.kdrt,
        payload.nikah,
        payload.tempatlahir,
        payload.tgllahir,
        payload.tglregistrasi,
        payload.nokk,
        payload.nobpjs,
        payload.goldarah,
        payload.email,
        payload.pendidikan,
        payload.jeniskelamin,
        payload.dusun,
        payload.pekerjaan,
        payload.namaayah,
        payload.namaibu,
        payload.negara,
        payload.statwn,
        payload.statint,
        payload.tglint,
        payload.ket,
        payload.created_by,
        payload.updated_by,
    )


@router.get("/", response_model=list[MasterKtpResponse])
def get_masterktps(uc: MasterKtpUseCase = Depends(get_usecase)):
    return uc.get_all()


@router.get("/{idktp}", response_model=MasterKtpResponse)
def get_masterktp(
    idktp: int,
    uc: MasterKtpUseCase = Depends(get_usecase),
):
    master_ktp = uc.get_by_id(idktp)
    if not master_ktp:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MasterKtp not found",
        )
    return master_ktp


@router.put("/{idktp}", response_model=MasterKtpResponse)
def update_masterktp(
    idktp: int,
    payload: MasterKtpUpdate,
    uc: MasterKtpUseCase = Depends(get_usecase),
):
    master_ktp = uc.update(
        idktp,
        payload.nik,
        payload.nama,
        payload.nohp,
        payload.alamat,
        payload.idkabkokta,
        payload.idkecamatan,
        payload.idkelurahan,
        payload.agama,
        payload.tgldaftar,
        payload.idprovinsi,
        payload.idrw,
        payload.idrt,
        payload.kdrt,
        payload.nikah,
        payload.tempatlahir,
        payload.tgllahir,
        payload.tglregistrasi,
        payload.nokk,
        payload.nobpjs,
        payload.goldarah,
        payload.email,
        payload.pendidikan,
        payload.jeniskelamin,
        payload.dusun,
        payload.pekerjaan,
        payload.namaayah,
        payload.namaibu,
        payload.negara,
        payload.statwn,
        payload.statint,
        payload.tglint,
        payload.ket,
        payload.updated_by,
    )
    if not master_ktp:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MasterKtp not found",
        )
    return master_ktp


@router.delete("/{idktp}")
def delete_masterktp(
    idktp: int,
    uc: MasterKtpUseCase = Depends(get_usecase),
):
    deleted = uc.delete(idktp)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MasterKtp not found",
        )
    return {"message": "Deleted"}
