from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.infrastructure.repositories.transpenetapan_repository_impl import (
    TransPenetapanRepositoryImpl,
)
from app.schemas.transpenetapan_schema import (
    TransPenetapanCreate,
    TransPenetapanResponse,
    TransPenetapanUpdate,
)
from app.usecases.transpenetapan_usecase import TransPenetapanUseCase

router = APIRouter(prefix="/api/v1/transpenetapan", tags=["transpenetapan"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_usecase(db: Session = Depends(get_db)):
    repo = TransPenetapanRepositoryImpl(db)
    return TransPenetapanUseCase(repo)


@router.post("/", response_model=TransPenetapanResponse)
def create_transpenetapan(
    payload: TransPenetapanCreate,
    uc: TransPenetapanUseCase = Depends(get_usecase),
):
    return uc.create(
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


@router.get("/", response_model=list[TransPenetapanResponse])
def get_transpenetapan(uc: TransPenetapanUseCase = Depends(get_usecase)):
    return uc.get_all()


@router.get("/{idpenetapan}", response_model=TransPenetapanResponse)
def get_transpenetapan_by_id(
    idpenetapan: int,
    uc: TransPenetapanUseCase = Depends(get_usecase),
):
    trans_penetapan = uc.get_by_id(idpenetapan)
    if not trans_penetapan:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="TransPenetapan not found",
        )
    return trans_penetapan


@router.put("/{idpenetapan}", response_model=TransPenetapanResponse)
def update_transpenetapan(
    idpenetapan: int,
    payload: TransPenetapanUpdate,
    uc: TransPenetapanUseCase = Depends(get_usecase),
):
    trans_penetapan = uc.update(
        idpenetapan,
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
    if not trans_penetapan:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="TransPenetapan not found",
        )
    return trans_penetapan


@router.delete("/{idpenetapan}")
def delete_transpenetapan(
    idpenetapan: int,
    uc: TransPenetapanUseCase = Depends(get_usecase),
):
    deleted = uc.delete(idpenetapan)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="TransPenetapan not found",
        )
    return {"message": "Deleted"}
