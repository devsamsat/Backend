from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.infrastructure.repositories.transpendataan_repository_impl import (
    TransPendataanRepositoryImpl,
)
from app.schemas.transpendataan_schema import (
    TransPendataanCreate,
    TransPendataanResponse,
    TransPendataanUpdate,
)
from app.usecases.transpendataan_usecase import TransPendataanUseCase

router = APIRouter(prefix="/api/v1/transpendataan", tags=["transpendataan"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_usecase(db: Session = Depends(get_db)):
    repo = TransPendataanRepositoryImpl(db)
    return TransPendataanUseCase(repo)


@router.post("/", response_model=TransPendataanResponse)
def create_transpendataan(
    payload: TransPendataanCreate,
    uc: TransPendataanUseCase = Depends(get_usecase),
):
    return uc.create(
        payload.spt,
        payload.idwpdata,
        payload.uruttgl,
        payload.tarifpjk,
        payload.idupt,
        payload.status,
        payload.tglpendataan,
        payload.masaawal,
        payload.masaakhir,
        payload.jmlomzetawal,
        payload.kdflow,
        payload.created_by,
        payload.updated_by,
    )


@router.get("/", response_model=list[TransPendataanResponse])
def get_transpendataan(uc: TransPendataanUseCase = Depends(get_usecase)):
    return uc.get_all()


@router.get("/{idpendataan}", response_model=TransPendataanResponse)
def get_transpendataan_by_id(
    idpendataan: int,
    uc: TransPendataanUseCase = Depends(get_usecase),
):
    trans_pendataan = uc.get_by_id(idpendataan)
    if not trans_pendataan:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="TransPendataan not found",
        )
    return trans_pendataan


@router.put("/{idpendataan}", response_model=TransPendataanResponse)
def update_transpendataan(
    idpendataan: int,
    payload: TransPendataanUpdate,
    uc: TransPendataanUseCase = Depends(get_usecase),
):
    trans_pendataan = uc.update(
        idpendataan,
        payload.spt,
        payload.idwpdata,
        payload.uruttgl,
        payload.tarifpjk,
        payload.idupt,
        payload.status,
        payload.tglpendataan,
        payload.masaawal,
        payload.masaakhir,
        payload.jmlomzetawal,
        payload.kdflow,
        payload.updated_by,
    )
    if not trans_pendataan:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="TransPendataan not found",
        )
    return trans_pendataan


@router.delete("/{idpendataan}")
def delete_transpendataan(
    idpendataan: int,
    uc: TransPendataanUseCase = Depends(get_usecase),
):
    deleted = uc.delete(idpendataan)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="TransPendataan not found",
        )
    return {"message": "Deleted"}
