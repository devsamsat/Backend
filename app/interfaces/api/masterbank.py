from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.infrastructure.repositories.masterbank_repository_impl import MasterBankRepositoryImpl
from app.usecases.masterbank_usecase import MasterBankUseCase
from app.schemas.masterbank_schema import (
    MasterBankCreate,
    MasterBankResponse,
    MasterBankUpdate,
)

router = APIRouter(prefix="/api/v1/masterbank", tags=["masterbank"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_usecase(db: Session = Depends(get_db)):
    repo = MasterBankRepositoryImpl(db)
    return MasterBankUseCase(repo)


@router.post("/", response_model=MasterBankResponse)
def create_masterbank(
    payload: MasterBankCreate,
    uc: MasterBankUseCase = Depends(get_usecase),
):
    return uc.create(
        payload.kodebank,
        payload.namabank,
        payload.akronimbank,
        payload.cabangbank,
        payload.alamatbank,
        payload.status,
        payload.created_by,
        payload.updated_by,
    )


@router.get("/", response_model=list[MasterBankResponse])
def get_masterbanks(uc: MasterBankUseCase = Depends(get_usecase)):
    return uc.get_all()


@router.get("/{idbank}", response_model=MasterBankResponse)
def get_masterbank(idbank: int, uc: MasterBankUseCase = Depends(get_usecase)):
    master_bank = uc.get_by_id(idbank)
    if not master_bank:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MasterBank not found",
        )
    return master_bank


@router.put("/{idbank}", response_model=MasterBankResponse)
def update_masterbank(
    idbank: int,
    payload: MasterBankUpdate,
    uc: MasterBankUseCase = Depends(get_usecase),
):
    master_bank = uc.update(
        idbank,
        payload.kodebank,
        payload.namabank,
        payload.akronimbank,
        payload.cabangbank,
        payload.alamatbank,
        payload.status,
        payload.updated_by,
    )
    if not master_bank:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MasterBank not found",
        )
    return master_bank


@router.delete("/{idbank}")
def delete_masterbank(idbank: int, uc: MasterBankUseCase = Depends(get_usecase)):
    deleted = uc.delete(idbank)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MasterBank not found",
        )
    return {"message": "Deleted"}
