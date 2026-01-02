from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.infrastructure.repositories.transhistpendataan_repository_impl import (
    TransHistPendataanRepositoryImpl,
)
from app.schemas.transhistpendataan_schema import (
    TransHistPendataanCreate,
    TransHistPendataanResponse,
    TransHistPendataanUpdate,
)
from app.usecases.transhistpendataan_usecase import TransHistPendataanUseCase

router = APIRouter(prefix="/api/v1/transhistpendataan", tags=["transhistpendataan"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_usecase(db: Session = Depends(get_db)):
    repo = TransHistPendataanRepositoryImpl(db)
    return TransHistPendataanUseCase(repo)


@router.post("/", response_model=TransHistPendataanResponse)
def create_transhistpendataan(
    payload: TransHistPendataanCreate,
    uc: TransHistPendataanUseCase = Depends(get_usecase),
):
    return uc.create(
        payload.idpendataan,
        payload.spt,
        payload.idwpdata,
        payload.uruttgl,
        payload.tarifpjk,
        payload.idupt,
        payload.histid,
        payload.status,
        payload.tglpendataan,
        payload.masaawal,
        payload.masaakhir,
        payload.jmlomzetawal,
        payload.kdflow,
        payload.created_by,
        payload.updated_by,
    )


@router.get("/", response_model=list[TransHistPendataanResponse])
def get_transhistpendataan(
    uc: TransHistPendataanUseCase = Depends(get_usecase),
):
    return uc.get_all()


@router.get("/{idhistpendataan}", response_model=TransHistPendataanResponse)
def get_transhistpendataan_by_id(
    idhistpendataan: int,
    uc: TransHistPendataanUseCase = Depends(get_usecase),
):
    trans_hist_pendataan = uc.get_by_id(idhistpendataan)
    if not trans_hist_pendataan:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="TransHistPendataan not found",
        )
    return trans_hist_pendataan


@router.put("/{idhistpendataan}", response_model=TransHistPendataanResponse)
def update_transhistpendataan(
    idhistpendataan: int,
    payload: TransHistPendataanUpdate,
    uc: TransHistPendataanUseCase = Depends(get_usecase),
):
    trans_hist_pendataan = uc.update(
        idhistpendataan,
        payload.idpendataan,
        payload.spt,
        payload.idwpdata,
        payload.uruttgl,
        payload.tarifpjk,
        payload.idupt,
        payload.histid,
        payload.status,
        payload.tglpendataan,
        payload.masaawal,
        payload.masaakhir,
        payload.jmlomzetawal,
        payload.kdflow,
        payload.updated_by,
    )
    if not trans_hist_pendataan:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="TransHistPendataan not found",
        )
    return trans_hist_pendataan


@router.delete("/{idhistpendataan}")
def delete_transhistpendataan(
    idhistpendataan: int,
    uc: TransHistPendataanUseCase = Depends(get_usecase),
):
    deleted = uc.delete(idhistpendataan)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="TransHistPendataan not found",
        )
    return {"message": "Deleted"}
