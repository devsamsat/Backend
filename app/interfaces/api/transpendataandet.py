from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.infrastructure.repositories.transpendataandet_repository_impl import (
    TransPendataanDetRepositoryImpl,
)
from app.schemas.transpendataandet_schema import (
    TransPendataanDetCreate,
    TransPendataanDetResponse,
    TransPendataanDetUpdate,
)
from app.usecases.transpendataandet_usecase import TransPendataanDetUseCase

router = APIRouter(prefix="/api/v1/transpendataandet", tags=["transpendataandet"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_usecase(db: Session = Depends(get_db)):
    repo = TransPendataanDetRepositoryImpl(db)
    return TransPendataanDetUseCase(repo)


@router.post("/", response_model=TransPendataanDetResponse)
def create_transpendataandet(
    payload: TransPendataanDetCreate,
    uc: TransPendataanDetUseCase = Depends(get_usecase),
):
    return uc.create(
        payload.idpendataan,
        payload.idpenetapan,
        payload.nourut,
        payload.transid,
        payload.ket1,
        payload.usahaid,
        payload.tarifpajak,
        payload.status,
        payload.lokasi,
        payload.created_by,
        payload.updated_by,
    )


@router.get("/", response_model=list[TransPendataanDetResponse])
def get_transpendataandet(uc: TransPendataanDetUseCase = Depends(get_usecase)):
    return uc.get_all()


@router.get("/{idpendataandet}", response_model=TransPendataanDetResponse)
def get_transpendataandet_by_id(
    idpendataandet: int,
    uc: TransPendataanDetUseCase = Depends(get_usecase),
):
    trans_pendataan_det = uc.get_by_id(idpendataandet)
    if not trans_pendataan_det:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="TransPendataanDet not found",
        )
    return trans_pendataan_det


@router.put("/{idpendataandet}", response_model=TransPendataanDetResponse)
def update_transpendataandet(
    idpendataandet: int,
    payload: TransPendataanDetUpdate,
    uc: TransPendataanDetUseCase = Depends(get_usecase),
):
    trans_pendataan_det = uc.update(
        idpendataandet,
        payload.idpendataan,
        payload.idpenetapan,
        payload.nourut,
        payload.transid,
        payload.ket1,
        payload.usahaid,
        payload.tarifpajak,
        payload.status,
        payload.lokasi,
        payload.updated_by,
    )
    if not trans_pendataan_det:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="TransPendataanDet not found",
        )
    return trans_pendataan_det


@router.delete("/{idpendataandet}")
def delete_transpendataandet(
    idpendataandet: int,
    uc: TransPendataanDetUseCase = Depends(get_usecase),
):
    deleted = uc.delete(idpendataandet)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="TransPendataanDet not found",
        )
    return {"message": "Deleted"}
