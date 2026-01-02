from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.infrastructure.repositories.masterrt_repository_impl import MasterRtRepositoryImpl
from app.usecases.masterrt_usecase import MasterRtUseCase
from app.schemas.masterrt_schema import (
    MasterRtCreate,
    MasterRtResponse,
    MasterRtUpdate,
)

router = APIRouter(prefix="/api/v1/masterrt", tags=["masterrt"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_usecase(db: Session = Depends(get_db)):
    repo = MasterRtRepositoryImpl(db)
    return MasterRtUseCase(repo)


@router.post("/", response_model=MasterRtResponse)
def create_masterrt(
    payload: MasterRtCreate,
    uc: MasterRtUseCase = Depends(get_usecase),
):
    return uc.create(
        payload.idrw,
        payload.status,
        payload.kdrt,
        payload.created_by,
        payload.updated_by,
    )


@router.get("/", response_model=list[MasterRtResponse])
def get_masterrts(uc: MasterRtUseCase = Depends(get_usecase)):
    return uc.get_all()


@router.get("/{idrt}", response_model=MasterRtResponse)
def get_masterrt(idrt: int, uc: MasterRtUseCase = Depends(get_usecase)):
    master_rt = uc.get_by_id(idrt)
    if not master_rt:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MasterRt not found",
        )
    return master_rt


@router.put("/{idrt}", response_model=MasterRtResponse)
def update_masterrt(
    idrt: int,
    payload: MasterRtUpdate,
    uc: MasterRtUseCase = Depends(get_usecase),
):
    master_rt = uc.update(
        idrt,
        payload.idrw,
        payload.status,
        payload.kdrt,
        payload.updated_by,
    )
    if not master_rt:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MasterRt not found",
        )
    return master_rt


@router.delete("/{idrt}")
def delete_masterrt(idrt: int, uc: MasterRtUseCase = Depends(get_usecase)):
    deleted = uc.delete(idrt)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MasterRt not found",
        )
    return {"message": "Deleted"}
