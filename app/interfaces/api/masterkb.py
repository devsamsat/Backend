from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.infrastructure.repositories.masterkb_repository_impl import MasterKbRepositoryImpl
from app.usecases.masterkb_usecase import MasterKbUseCase
from app.schemas.masterkb_schema import (
    MasterKbCreate,
    MasterKbResponse,
    MasterKbUpdate,
)

router = APIRouter(prefix="/api/v1/masterkb", tags=["masterkb"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_usecase(db: Session = Depends(get_db)):
    repo = MasterKbRepositoryImpl(db)
    return MasterKbUseCase(repo)


@router.post("/", response_model=MasterKbResponse)
def create_masterkb(
    payload: MasterKbCreate,
    uc: MasterKbUseCase = Depends(get_usecase),
):
    return uc.create(
        payload.namabadan,
        payload.insidentil,
        payload.kdplat,
        payload.nomorfaktur,
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


@router.get("/", response_model=list[MasterKbResponse])
def get_masterkbs(uc: MasterKbUseCase = Depends(get_usecase)):
    return uc.get_all()


@router.get("/{idkb}", response_model=MasterKbResponse)
def get_masterkb(
    idkb: int,
    uc: MasterKbUseCase = Depends(get_usecase),
):
    master_kb = uc.get_by_id(idkb)
    if not master_kb:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MasterKb not found",
        )
    return master_kb


@router.put("/{idkb}", response_model=MasterKbResponse)
def update_masterkb(
    idkb: int,
    payload: MasterKbUpdate,
    uc: MasterKbUseCase = Depends(get_usecase),
):
    master_kb = uc.update(
        idkb,
        payload.namabadan,
        payload.insidentil,
        payload.kdplat,
        payload.nomorfaktur,
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
    if not master_kb:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MasterKb not found",
        )
    return master_kb


@router.delete("/{idkb}")
def delete_masterkb(
    idkb: int,
    uc: MasterKbUseCase = Depends(get_usecase),
):
    deleted = uc.delete(idkb)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MasterKb not found",
        )
    return {"message": "Deleted"}
