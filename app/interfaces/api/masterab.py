from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.infrastructure.repositories.masterab_repository_impl import MasterAbRepositoryImpl
from app.usecases.masterab_usecase import MasterAbUseCase
from app.schemas.masterab_schema import (
    MasterAbCreate,
    MasterAbResponse,
    MasterAbUpdate,
)

router = APIRouter(prefix="/api/v1/masterab", tags=["masterab"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_usecase(db: Session = Depends(get_db)):
    repo = MasterAbRepositoryImpl(db)
    return MasterAbUseCase(repo)


@router.post("/", response_model=MasterAbResponse)
def create_masterab(
    payload: MasterAbCreate,
    uc: MasterAbUseCase = Depends(get_usecase),
):
    return uc.create(
        payload.nomorab,
        payload.namabadan,
        payload.insidentil,
        payload.kdplat,
        payload.alamat,
        payload.idkabkokta,
        payload.idkecamatan,
        payload.idkelurahan,
        payload.idrw,
        payload.idrt,
        payload.telepon,
        payload.fax,
        payload.idktp,
        payload.noktp,
        payload.pekerjaan,
        payload.tgldaftar,
        payload.tglfaktur,
        payload.jnskendid,
        payload.idmerk,
        payload.merk,
        payload.tipe,
        payload.tahunbuat,
        payload.kodebbm,
        payload.bbm,
        payload.cylinder,
        payload.norangka,
        payload.nomesin,
        payload.nobpkb,
        payload.kdmilik,
        payload.kdguna,
        payload.kendke,
        payload.warna,
        payload.created_by,
        payload.updated_by,
    )


@router.get("/", response_model=list[MasterAbResponse])
def get_masterabs(uc: MasterAbUseCase = Depends(get_usecase)):
    return uc.get_all()


@router.get("/{idab}", response_model=MasterAbResponse)
def get_masterab(idab: int, uc: MasterAbUseCase = Depends(get_usecase)):
    master_ab = uc.get_by_id(idab)
    if not master_ab:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MasterAb not found",
        )
    return master_ab


@router.put("/{idab}", response_model=MasterAbResponse)
def update_masterab(
    idab: int,
    payload: MasterAbUpdate,
    uc: MasterAbUseCase = Depends(get_usecase),
):
    master_ab = uc.update(
        idab,
        payload.nomorab,
        payload.namabadan,
        payload.insidentil,
        payload.kdplat,
        payload.alamat,
        payload.idkabkokta,
        payload.idkecamatan,
        payload.idkelurahan,
        payload.idrw,
        payload.idrt,
        payload.telepon,
        payload.fax,
        payload.idktp,
        payload.noktp,
        payload.pekerjaan,
        payload.tgldaftar,
        payload.tglfaktur,
        payload.jnskendid,
        payload.idmerk,
        payload.merk,
        payload.tipe,
        payload.tahunbuat,
        payload.kodebbm,
        payload.bbm,
        payload.cylinder,
        payload.norangka,
        payload.nomesin,
        payload.nobpkb,
        payload.kdmilik,
        payload.kdguna,
        payload.kendke,
        payload.warna,
        payload.updated_by,
    )
    if not master_ab:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MasterAb not found",
        )
    return master_ab


@router.delete("/{idab}")
def delete_masterab(idab: int, uc: MasterAbUseCase = Depends(get_usecase)):
    deleted = uc.delete(idab)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MasterAb not found",
        )
    return {"message": "Deleted"}
