from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.infrastructure.repositories.masterabdet_repository_impl import MasterAbDetRepositoryImpl
from app.usecases.masterabdet_usecase import MasterAbDetUseCase
from app.schemas.masterabdet_schema import (
    MasterAbDetCreate,
    MasterAbDetResponse,
    MasterAbDetUpdate,
)

router = APIRouter(prefix="/api/v1/masterabdet", tags=["masterabdet"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_usecase(db: Session = Depends(get_db)):
    repo = MasterAbDetRepositoryImpl(db)
    return MasterAbDetUseCase(repo)


@router.post("/", response_model=MasterAbDetResponse)
def create_masterabdet(
    payload: MasterAbDetCreate,
    uc: MasterAbDetUseCase = Depends(get_usecase),
):
    return uc.create(payload.idab, payload.idjnsd, payload.created_by, payload.updated_by)


@router.get("/", response_model=list[MasterAbDetResponse])
def get_masterabdets(uc: MasterAbDetUseCase = Depends(get_usecase)):
    return uc.get_all()


@router.get("/{idabdet}", response_model=MasterAbDetResponse)
def get_masterabdet(idabdet: int, uc: MasterAbDetUseCase = Depends(get_usecase)):
    master_ab_det = uc.get_by_id(idabdet)
    if not master_ab_det:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MasterAbDet not found",
        )
    return master_ab_det


@router.put("/{idabdet}", response_model=MasterAbDetResponse)
def update_masterabdet(
    idabdet: int,
    payload: MasterAbDetUpdate,
    uc: MasterAbDetUseCase = Depends(get_usecase),
):
    master_ab_det = uc.update(
        idabdet,
        payload.idab,
        payload.idjnsd,
        payload.updated_by,
    )
    if not master_ab_det:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MasterAbDet not found",
        )
    return master_ab_det


@router.delete("/{idabdet}")
def delete_masterabdet(idabdet: int, uc: MasterAbDetUseCase = Depends(get_usecase)):
    deleted = uc.delete(idabdet)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MasterAbDet not found",
        )
    return {"message": "Deleted"}
