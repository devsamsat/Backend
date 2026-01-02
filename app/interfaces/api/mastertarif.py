from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.infrastructure.repositories.mastertarif_repository_impl import (
    MasterTarifRepositoryImpl,
)
from app.usecases.mastertarif_usecase import MasterTarifUseCase
from app.schemas.mastertarif_schema import (
    MasterTarifCreate,
    MasterTarifResponse,
    MasterTarifUpdate,
)

router = APIRouter(prefix="/api/v1/mastertarif", tags=["mastertarif"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_usecase(db: Session = Depends(get_db)):
    repo = MasterTarifRepositoryImpl(db)
    return MasterTarifUseCase(repo)


@router.post("/", response_model=MasterTarifResponse)
def create_mastertarif(
    payload: MasterTarifCreate,
    uc: MasterTarifUseCase = Depends(get_usecase),
):
    return uc.create(
        payload.kdjnspjk,
        payload.jnskendid,
        payload.satuan,
        payload.awal,
        payload.akhir,
        payload.keterangan,
        payload.kdflow,
        payload.kdplat,
        payload.statumum,
        payload.tarif,
        payload.created_by,
        payload.updated_by,
    )


@router.get("/", response_model=list[MasterTarifResponse])
def get_mastertarifs(uc: MasterTarifUseCase = Depends(get_usecase)):
    return uc.get_all()


@router.get("/{idtarif}", response_model=MasterTarifResponse)
def get_mastertarif(idtarif: int, uc: MasterTarifUseCase = Depends(get_usecase)):
    master_tarif = uc.get_by_id(idtarif)
    if not master_tarif:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MasterTarif not found",
        )
    return master_tarif


@router.put("/{idtarif}", response_model=MasterTarifResponse)
def update_mastertarif(
    idtarif: int,
    payload: MasterTarifUpdate,
    uc: MasterTarifUseCase = Depends(get_usecase),
):
    master_tarif = uc.update(
        idtarif,
        payload.kdjnspjk,
        payload.jnskendid,
        payload.satuan,
        payload.awal,
        payload.akhir,
        payload.keterangan,
        payload.kdflow,
        payload.kdplat,
        payload.statumum,
        payload.tarif,
        payload.updated_by,
    )
    if not master_tarif:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MasterTarif not found",
        )
    return master_tarif


@router.delete("/{idtarif}")
def delete_mastertarif(idtarif: int, uc: MasterTarifUseCase = Depends(get_usecase)):
    deleted = uc.delete(idtarif)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MasterTarif not found",
        )
    return {"message": "Deleted"}
