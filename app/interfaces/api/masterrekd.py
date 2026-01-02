from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.infrastructure.repositories.masterrekd_repository_impl import MasterRekdRepositoryImpl
from app.usecases.masterrekd_usecase import MasterRekdUseCase
from app.schemas.masterrekd_schema import (
    MasterRekdCreate,
    MasterRekdResponse,
    MasterRekdUpdate,
)

router = APIRouter(prefix="/api/v1/masterrekd", tags=["masterrekd"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_usecase(db: Session = Depends(get_db)):
    repo = MasterRekdRepositoryImpl(db)
    return MasterRekdUseCase(repo)


@router.post("/", response_model=MasterRekdResponse)
def create_masterrekd(
    payload: MasterRekdCreate,
    uc: MasterRekdUseCase = Depends(get_usecase),
):
    return uc.create(
        payload.kdrek,
        payload.idparent,
        payload.mtglevel,
        payload.nmrek,
        payload.kdjnspjk,
        payload.rek_type,
        payload.status,
        payload.created_by,
        payload.updated_by,
    )


@router.get("/", response_model=list[MasterRekdResponse])
def get_masterrekds(uc: MasterRekdUseCase = Depends(get_usecase)):
    return uc.get_all()


@router.get("/{idrekd}", response_model=MasterRekdResponse)
def get_masterrekd(idrekd: int, uc: MasterRekdUseCase = Depends(get_usecase)):
    master_rekd = uc.get_by_id(idrekd)
    if not master_rekd:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MasterRekd not found",
        )
    return master_rekd


@router.put("/{idrekd}", response_model=MasterRekdResponse)
def update_masterrekd(
    idrekd: int,
    payload: MasterRekdUpdate,
    uc: MasterRekdUseCase = Depends(get_usecase),
):
    master_rekd = uc.update(
        idrekd,
        payload.kdrek,
        payload.idparent,
        payload.mtglevel,
        payload.nmrek,
        payload.kdjnspjk,
        payload.rek_type,
        payload.status,
        payload.updated_by,
    )
    if not master_rekd:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MasterRekd not found",
        )
    return master_rekd


@router.delete("/{idrekd}")
def delete_masterrekd(idrekd: int, uc: MasterRekdUseCase = Depends(get_usecase)):
    deleted = uc.delete(idrekd)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MasterRekd not found",
        )
    return {"message": "Deleted"}
