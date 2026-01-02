from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.infrastructure.repositories.masterrw_repository_impl import MasterRwRepositoryImpl
from app.usecases.masterrw_usecase import MasterRwUseCase
from app.schemas.masterrw_schema import (
    MasterRwCreate,
    MasterRwResponse,
    MasterRwUpdate,
)

router = APIRouter(prefix="/api/v1/masterrw", tags=["masterrw"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_usecase(db: Session = Depends(get_db)):
    repo = MasterRwRepositoryImpl(db)
    return MasterRwUseCase(repo)


@router.post("/", response_model=MasterRwResponse)
def create_masterrw(
    payload: MasterRwCreate,
    uc: MasterRwUseCase = Depends(get_usecase),
):
    return uc.create(
        payload.idkelurahan,
        payload.alamat,
        payload.status,
        payload.kdrw,
        payload.created_by,
        payload.updated_by,
    )


@router.get("/", response_model=list[MasterRwResponse])
def get_masterrws(uc: MasterRwUseCase = Depends(get_usecase)):
    return uc.get_all()


@router.get("/{idrw}", response_model=MasterRwResponse)
def get_masterrw(idrw: int, uc: MasterRwUseCase = Depends(get_usecase)):
    master_rw = uc.get_by_id(idrw)
    if not master_rw:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MasterRw not found",
        )
    return master_rw


@router.put("/{idrw}", response_model=MasterRwResponse)
def update_masterrw(
    idrw: int,
    payload: MasterRwUpdate,
    uc: MasterRwUseCase = Depends(get_usecase),
):
    master_rw = uc.update(
        idrw,
        payload.idkelurahan,
        payload.alamat,
        payload.status,
        payload.kdrw,
        payload.updated_by,
    )
    if not master_rw:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MasterRw not found",
        )
    return master_rw


@router.delete("/{idrw}")
def delete_masterrw(idrw: int, uc: MasterRwUseCase = Depends(get_usecase)):
    deleted = uc.delete(idrw)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MasterRw not found",
        )
    return {"message": "Deleted"}
