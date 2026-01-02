from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.infrastructure.repositories.mastermerk_repository_impl import MasterMerkRepositoryImpl
from app.schemas.mastermerk_schema import (
    MasterMerkCreate,
    MasterMerkResponse,
    MasterMerkUpdate,
)
from app.usecases.mastermerk_usecase import MasterMerkUseCase

router = APIRouter(prefix="/api/v1/mastermerk", tags=["mastermerk"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_usecase(db: Session = Depends(get_db)):
    repo = MasterMerkRepositoryImpl(db)
    return MasterMerkUseCase(repo)


@router.post("/", response_model=MasterMerkResponse)
def create_mastermerk(
    payload: MasterMerkCreate,
    uc: MasterMerkUseCase = Depends(get_usecase),
):
    return uc.create(
        payload.kdmerk,
        payload.nmmerk,
        payload.keterangan,
        payload.status,
        payload.created_by,
        payload.updated_by,
    )


@router.get("/", response_model=list[MasterMerkResponse])
def get_mastermerks(uc: MasterMerkUseCase = Depends(get_usecase)):
    return uc.get_all()


@router.get("/{idmerk}", response_model=MasterMerkResponse)
def get_mastermerk(idmerk: int, uc: MasterMerkUseCase = Depends(get_usecase)):
    record = uc.get_by_id(idmerk)
    if not record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MasterMerk not found",
        )
    return record


@router.put("/{idmerk}", response_model=MasterMerkResponse)
def update_mastermerk(
    idmerk: int,
    payload: MasterMerkUpdate,
    uc: MasterMerkUseCase = Depends(get_usecase),
):
    record = uc.update(
        idmerk,
        payload.kdmerk,
        payload.nmmerk,
        payload.keterangan,
        payload.status,
        payload.updated_by,
    )
    if not record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MasterMerk not found",
        )
    return record


@router.delete("/{idmerk}")
def delete_mastermerk(idmerk: int, uc: MasterMerkUseCase = Depends(get_usecase)):
    deleted = uc.delete(idmerk)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MasterMerk not found",
        )
    return {"message": "Deleted"}
