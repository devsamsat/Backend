from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.infrastructure.repositories.transstsdet_repository_impl import (
    TransStsDetRepositoryImpl,
)
from app.schemas.transstsdet_schema import (
    TransStsDetCreate,
    TransStsDetResponse,
    TransStsDetUpdate,
)
from app.usecases.transstsdet_usecase import TransStsDetUseCase

router = APIRouter(prefix="/api/v1/transstsdet", tags=["transstsdet"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_usecase(db: Session = Depends(get_db)):
    repo = TransStsDetRepositoryImpl(db)
    return TransStsDetUseCase(repo)


@router.post("/", response_model=TransStsDetResponse)
def create_transstsdet(
    payload: TransStsDetCreate,
    uc: TransStsDetUseCase = Depends(get_usecase),
):
    return uc.create(
        payload.idsts,
        payload.idrekd,
        payload.nilaists,
        payload.jenis,
        payload.created_by,
        payload.updated_by,
    )


@router.get("/", response_model=list[TransStsDetResponse])
def get_transstsdet(uc: TransStsDetUseCase = Depends(get_usecase)):
    return uc.get_all()


@router.get("/{idstsdet}", response_model=TransStsDetResponse)
def get_transstsdet_by_id(
    idstsdet: int,
    uc: TransStsDetUseCase = Depends(get_usecase),
):
    trans_sts_det = uc.get_by_id(idstsdet)
    if not trans_sts_det:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="TransStsDet not found",
        )
    return trans_sts_det


@router.put("/{idstsdet}", response_model=TransStsDetResponse)
def update_transstsdet(
    idstsdet: int,
    payload: TransStsDetUpdate,
    uc: TransStsDetUseCase = Depends(get_usecase),
):
    trans_sts_det = uc.update(
        idstsdet,
        payload.idsts,
        payload.idrekd,
        payload.nilaists,
        payload.jenis,
        payload.updated_by,
    )
    if not trans_sts_det:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="TransStsDet not found",
        )
    return trans_sts_det


@router.delete("/{idstsdet}")
def delete_transstsdet(
    idstsdet: int,
    uc: TransStsDetUseCase = Depends(get_usecase),
):
    deleted = uc.delete(idstsdet)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="TransStsDet not found",
        )
    return {"message": "Deleted"}
