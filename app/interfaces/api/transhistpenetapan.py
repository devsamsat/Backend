from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.infrastructure.repositories.transhistpenetapan_repository_impl import (
    TransHistPenetapanRepositoryImpl,
)
from app.schemas.transhistpenetapan_schema import (
    TransHistPenetapanCreate,
    TransHistPenetapanResponse,
    TransHistPenetapanUpdate,
)
from app.usecases.transhistpenetapan_usecase import TransHistPenetapanUseCase

router = APIRouter(prefix="/api/v1/transhistpenetapan", tags=["transhistpenetapan"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_usecase(db: Session = Depends(get_db)):
    repo = TransHistPenetapanRepositoryImpl(db)
    return TransHistPenetapanUseCase(repo)


@router.post("/", response_model=TransHistPenetapanResponse)
def create_transhistpenetapan(
    payload: TransHistPenetapanCreate,
    uc: TransHistPenetapanUseCase = Depends(get_usecase),
):
    return uc.create(
        payload.idpenetapan,
        payload.idkohir,
        payload.idwpdata,
        payload.uruttgl,
        payload.tarifpajak,
        payload.statbayar,
        payload.status,
        payload.nokohir,
        payload.tglpenetapan,
        payload.tgljatuhtempo,
        payload.masaawal,
        payload.masaakhir,
        payload.jmlomzetawal,
        payload.denda,
        payload.kenaikan,
        payload.tglbayar,
        payload.jmlbayar,
        payload.tglkurangbayar,
        payload.jmlkurangbayar,
        payload.jmlperingatan,
        payload.kdflow,
        payload.opsid,
        payload.opsprov,
        payload.opskota,
        payload.dendaopsprov,
        payload.dendaopskota,
        payload.created_by,
        payload.updated_by,
    )


@router.get("/", response_model=list[TransHistPenetapanResponse])
def get_transhistpenetapan(
    uc: TransHistPenetapanUseCase = Depends(get_usecase),
):
    return uc.get_all()


@router.get("/{idhistpenetapan}", response_model=TransHistPenetapanResponse)
def get_transhistpenetapan_by_id(
    idhistpenetapan: int,
    uc: TransHistPenetapanUseCase = Depends(get_usecase),
):
    trans_hist_penetapan = uc.get_by_id(idhistpenetapan)
    if not trans_hist_penetapan:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="TransHistPenetapan not found",
        )
    return trans_hist_penetapan


@router.put("/{idhistpenetapan}", response_model=TransHistPenetapanResponse)
def update_transhistpenetapan(
    idhistpenetapan: int,
    payload: TransHistPenetapanUpdate,
    uc: TransHistPenetapanUseCase = Depends(get_usecase),
):
    trans_hist_penetapan = uc.update(
        idhistpenetapan,
        payload.idpenetapan,
        payload.idkohir,
        payload.idwpdata,
        payload.uruttgl,
        payload.tarifpajak,
        payload.statbayar,
        payload.status,
        payload.nokohir,
        payload.tglpenetapan,
        payload.tgljatuhtempo,
        payload.masaawal,
        payload.masaakhir,
        payload.jmlomzetawal,
        payload.denda,
        payload.kenaikan,
        payload.tglbayar,
        payload.jmlbayar,
        payload.tglkurangbayar,
        payload.jmlkurangbayar,
        payload.jmlperingatan,
        payload.kdflow,
        payload.opsid,
        payload.opsprov,
        payload.opskota,
        payload.dendaopsprov,
        payload.dendaopskota,
        payload.updated_by,
    )
    if not trans_hist_penetapan:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="TransHistPenetapan not found",
        )
    return trans_hist_penetapan


@router.delete("/{idhistpenetapan}")
def delete_transhistpenetapan(
    idhistpenetapan: int,
    uc: TransHistPenetapanUseCase = Depends(get_usecase),
):
    deleted = uc.delete(idhistpenetapan)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="TransHistPenetapan not found",
        )
    return {"message": "Deleted"}
