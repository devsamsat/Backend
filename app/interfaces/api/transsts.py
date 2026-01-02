from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.infrastructure.repositories.transsts_repository_impl import (
    TransStsRepositoryImpl,
)
from app.schemas.transsts_schema import TransStsCreate, TransStsResponse, TransStsUpdate
from app.usecases.transsts_usecase import TransStsUseCase

router = APIRouter(prefix="/api/v1/transsts", tags=["transsts"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_usecase(db: Session = Depends(get_db)):
    repo = TransStsRepositoryImpl(db)
    return TransStsUseCase(repo)


@router.post("/", response_model=TransStsResponse)
def create_transsts(
    payload: TransStsCreate,
    uc: TransStsUseCase = Depends(get_usecase),
):
    return uc.create(
        payload.idupt,
        payload.idbend,
        payload.nosts,
        payload.keterangan,
        payload.statbayar,
        payload.setorandari,
        payload.tglsts,
        payload.ntpd,
        payload.tglntpd,
        payload.statsts,
        payload.created_by,
        payload.updated_by,
    )


@router.get("/", response_model=list[TransStsResponse])
def get_transsts(uc: TransStsUseCase = Depends(get_usecase)):
    return uc.get_all()


@router.get("/{idsts}", response_model=TransStsResponse)
def get_transsts_by_id(idsts: int, uc: TransStsUseCase = Depends(get_usecase)):
    trans_sts = uc.get_by_id(idsts)
    if not trans_sts:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="TransSts not found",
        )
    return trans_sts


@router.put("/{idsts}", response_model=TransStsResponse)
def update_transsts(
    idsts: int,
    payload: TransStsUpdate,
    uc: TransStsUseCase = Depends(get_usecase),
):
    trans_sts = uc.update(
        idsts,
        payload.idupt,
        payload.idbend,
        payload.nosts,
        payload.keterangan,
        payload.statbayar,
        payload.setorandari,
        payload.tglsts,
        payload.ntpd,
        payload.tglntpd,
        payload.statsts,
        payload.updated_by,
    )
    if not trans_sts:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="TransSts not found",
        )
    return trans_sts


@router.delete("/{idsts}")
def delete_transsts(idsts: int, uc: TransStsUseCase = Depends(get_usecase)):
    deleted = uc.delete(idsts)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="TransSts not found",
        )
    return {"message": "Deleted"}
