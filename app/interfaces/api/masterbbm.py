from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.infrastructure.repositories.masterbbm_repository_impl import MasterBbmRepositoryImpl
from app.usecases.masterbbm_usecase import MasterBbmUseCase
from app.schemas.masterbbm_schema import (
    MasterBbmCreate,
    MasterBbmResponse,
    MasterBbmUpdate,
)

router = APIRouter(prefix="/api/v1/masterbbm", tags=["masterbbm"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_usecase(db: Session = Depends(get_db)):
    repo = MasterBbmRepositoryImpl(db)
    return MasterBbmUseCase(repo)


@router.post("/", response_model=MasterBbmResponse)
def create_masterbbm(
    payload: MasterBbmCreate,
    uc: MasterBbmUseCase = Depends(get_usecase),
):
    return uc.create(
        payload.kodebbm,
        payload.namabbm,
        payload.keterangan,
        payload.created_by,
        payload.updated_by,
    )


@router.get("/", response_model=list[MasterBbmResponse])
def get_masterbbms(uc: MasterBbmUseCase = Depends(get_usecase)):
    return uc.get_all()


@router.get("/{kodebbm}", response_model=MasterBbmResponse)
def get_masterbbm(kodebbm: str, uc: MasterBbmUseCase = Depends(get_usecase)):
    master_bbm = uc.get_by_id(kodebbm)
    if not master_bbm:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MasterBbm not found",
        )
    return master_bbm


@router.put("/{kodebbm}", response_model=MasterBbmResponse)
def update_masterbbm(
    kodebbm: str,
    payload: MasterBbmUpdate,
    uc: MasterBbmUseCase = Depends(get_usecase),
):
    master_bbm = uc.update(
        kodebbm,
        payload.namabbm,
        payload.keterangan,
        payload.updated_by,
    )
    if not master_bbm:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MasterBbm not found",
        )
    return master_bbm


@router.delete("/{kodebbm}")
def delete_masterbbm(kodebbm: str, uc: MasterBbmUseCase = Depends(get_usecase)):
    deleted = uc.delete(kodebbm)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MasterBbm not found",
        )
    return {"message": "Deleted"}
