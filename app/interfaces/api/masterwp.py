from datetime import date

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.infrastructure.repositories.masterwp_repository_impl import MasterWpRepositoryImpl
from app.usecases.masterwp_usecase import MasterWpUseCase
from app.schemas.masterwp_schema import MasterWpCreate, MasterWpResponse, MasterWpUpdate

router = APIRouter(prefix="/api/v1/masterwp", tags=["masterwp"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_usecase(db: Session = Depends(get_db)):
    repo = MasterWpRepositoryImpl(db)
    return MasterWpUseCase(repo)


@router.post("/", response_model=MasterWpResponse)
def create_masterwp(
    payload: MasterWpCreate,
    uc: MasterWpUseCase = Depends(get_usecase),
):
    return uc.create(
        payload.objekbadanno,
        payload.namabadan,
        payload.insidentil,
        payload.nopollama,
        payload.kdplat,
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


@router.get("/", response_model=list[MasterWpResponse])
def get_masterwps(
    nopollama: str | None = None,
    namapemilik: str | None = None,
    nikpemilik: str | None = None,
    alamat: str | None = None,
    kelurahan: str | None = None,
    kecamatan: str | None = None,
    kode_polisi: str | None = Query(None, alias="kode_polisi"),
    nostnkb: str | None = None,
    nobpkb: str | None = None,
    tgljualbeli: date | None = None,
    tgldaftar: date | None = None,
    norangka: str | None = None,
    nomesin: str | None = None,
    warna: str | None = None,
    is_match: bool = False,
    page: int = Query(1, ge=1),
    limit: int = Query(20, ge=1, le=200),
    uc: MasterWpUseCase = Depends(get_usecase),
):
    filters = {
        "nopollama": nopollama,
        "namapemilik": namapemilik,
        "nikpemilik": nikpemilik,
        "alamat": alamat,
        "kelurahan": kelurahan,
        "kecamatan": kecamatan,
        "kodepolisi": kode_polisi,
        "nostnkb": nostnkb,
        "nobpkb": nobpkb,
        "tgljualbeli": tgljualbeli,
        "tgldaftar": tgldaftar,
        "norangka": norangka,
        "nomesin": nomesin,
        "warna": warna,
        "is_match": is_match,
    }
    return uc.get_all(filters=filters, page=page, limit=limit)


@router.get("/{idwp}", response_model=MasterWpResponse)
def get_masterwp(idwp: int, uc: MasterWpUseCase = Depends(get_usecase)):
    master_wp = uc.get_by_id(idwp)
    if not master_wp:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MasterWp not found",
        )
    return master_wp


@router.put("/{idwp}", response_model=MasterWpResponse)
def update_masterwp(
    idwp: int,
    payload: MasterWpUpdate,
    uc: MasterWpUseCase = Depends(get_usecase),
):
    master_wp = uc.update(
        idwp,
        payload.objekbadanno,
        payload.namabadan,
        payload.insidentil,
        payload.nopollama,
        payload.kdplat,
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
    if not master_wp:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MasterWp not found",
        )
    return master_wp


@router.delete("/{idwp}")
def delete_masterwp(idwp: int, uc: MasterWpUseCase = Depends(get_usecase)):
    deleted = uc.delete(idwp)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MasterWp not found",
        )
    return {"message": "Deleted"}
