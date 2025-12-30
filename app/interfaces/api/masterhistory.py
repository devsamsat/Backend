from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.infrastructure.repositories.masterhistory_repository_impl import (
    MasterHistoryRepositoryImpl,
)
from app.usecases.masterhistory_usecase import MasterHistoryUseCase
from app.schemas.masterhistory_schema import (
    MasterHistoryCreate,
    MasterHistoryResponse,
    MasterHistoryUpdate,
)

router = APIRouter(prefix="/api/v1/masterhistory", tags=["masterhistory"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_usecase(db: Session = Depends(get_db)):
    repo = MasterHistoryRepositoryImpl(db)
    return MasterHistoryUseCase(repo)


@router.post("/", response_model=MasterHistoryResponse)
def create_masterhistory(
    payload: MasterHistoryCreate,
    uc: MasterHistoryUseCase = Depends(get_usecase),
):
    return uc.create(
        payload.idwp,
        payload.objekbadanno,
        payload.namabadan,
        payload.insidentil,
        payload.nopollama,
        payload.kdplat,
        payload.histid,
        payload.idgroupusaha,
        payload.kodepolisi,
        payload.kodelokasi,
        payload.idbadan,
        payload.idklasifikasi,
        payload.idlokasi,
        payload.alamat,
        payload.idkabkokta,
        payload.idkecamatan,
        payload.idkelurahan,
        payload.idrw,
        payload.idrt,
        payload.telepon,
        payload.fax,
        payload.namapemilik,
        payload.idktp,
        payload.pekerjaan,
        payload.tgldaftar,
        payload.tglsah,
        payload.keteblokir,
        payload.tglhapus,
        payload.groupblokir,
        payload.lastskp,
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
        payload.nostnkb,
        payload.daftarstnk,
        payload.tglcetakstnk,
        payload.tglstnk,
        payload.sdstnk,
        payload.tglskp,
        payload.awalskp,
        payload.akhirskp,
        payload.tglmutasi,
        payload.tgljualbeli,
        payload.nodaftar,
        payload.nosah1,
        payload.tglsah1,
        payload.nosah2,
        payload.tglsah2,
        payload.nosah3,
        payload.tglsah3,
        payload.nosah4,
        payload.tglsah4,
        payload.laporjual,
        payload.nikpemilik,
        payload.notelppemilik,
        payload.putih,
        payload.status,
        payload.statint,
        payload.created_by,
        payload.updated_by,
    )


@router.get("/", response_model=list[MasterHistoryResponse])
def get_masterhistories(uc: MasterHistoryUseCase = Depends(get_usecase)):
    return uc.get_all()


@router.get("/{idhistory}", response_model=MasterHistoryResponse)
def get_masterhistory(
    idhistory: int,
    uc: MasterHistoryUseCase = Depends(get_usecase),
):
    master_history = uc.get_by_id(idhistory)
    if not master_history:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MasterHistory not found",
        )
    return master_history


@router.put("/{idhistory}", response_model=MasterHistoryResponse)
def update_masterhistory(
    idhistory: int,
    payload: MasterHistoryUpdate,
    uc: MasterHistoryUseCase = Depends(get_usecase),
):
    master_history = uc.update(
        idhistory,
        payload.idwp,
        payload.objekbadanno,
        payload.namabadan,
        payload.insidentil,
        payload.nopollama,
        payload.kdplat,
        payload.histid,
        payload.idgroupusaha,
        payload.kodepolisi,
        payload.kodelokasi,
        payload.idbadan,
        payload.idklasifikasi,
        payload.idlokasi,
        payload.alamat,
        payload.idkabkokta,
        payload.idkecamatan,
        payload.idkelurahan,
        payload.idrw,
        payload.idrt,
        payload.telepon,
        payload.fax,
        payload.namapemilik,
        payload.idktp,
        payload.pekerjaan,
        payload.tgldaftar,
        payload.tglsah,
        payload.keteblokir,
        payload.tglhapus,
        payload.groupblokir,
        payload.lastskp,
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
        payload.nostnkb,
        payload.daftarstnk,
        payload.tglcetakstnk,
        payload.tglstnk,
        payload.sdstnk,
        payload.tglskp,
        payload.awalskp,
        payload.akhirskp,
        payload.tglmutasi,
        payload.tgljualbeli,
        payload.nodaftar,
        payload.nosah1,
        payload.tglsah1,
        payload.nosah2,
        payload.tglsah2,
        payload.nosah3,
        payload.tglsah3,
        payload.nosah4,
        payload.tglsah4,
        payload.laporjual,
        payload.nikpemilik,
        payload.notelppemilik,
        payload.putih,
        payload.status,
        payload.statint,
        payload.updated_by,
    )
    if not master_history:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MasterHistory not found",
        )
    return master_history


@router.delete("/{idhistory}")
def delete_masterhistory(
    idhistory: int,
    uc: MasterHistoryUseCase = Depends(get_usecase),
):
    deleted = uc.delete(idhistory)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MasterHistory not found",
        )
    return {"message": "Deleted"}
