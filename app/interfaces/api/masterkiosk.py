from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.infrastructure.repositories.masterkiosk_repository_impl import (
    MasterKioskRepositoryImpl,
)
from app.usecases.masterkiosk_usecase import MasterKioskUseCase
from app.schemas.masterkiosk_schema import (
    MasterKioskCreate,
    MasterKioskResponse,
    MasterKioskUpdate,
)

router = APIRouter(prefix="/api/v1/masterkiosk", tags=["masterkiosk"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_usecase(db: Session = Depends(get_db)):
    repo = MasterKioskRepositoryImpl(db)
    return MasterKioskUseCase(repo)


@router.post("/", response_model=MasterKioskResponse)
def create_masterkiosk(
    payload: MasterKioskCreate,
    uc: MasterKioskUseCase = Depends(get_usecase),
):
    return uc.create(
        payload.kodekiosk,
        payload.datakiosk,
        payload.level,
        payload.status,
        payload.idparent,
        payload.created_by,
        payload.updated_by,
    )


@router.get("/", response_model=list[MasterKioskResponse])
def get_masterkiosks(uc: MasterKioskUseCase = Depends(get_usecase)):
    return uc.get_all()


@router.get("/{idkios}", response_model=MasterKioskResponse)
def get_masterkiosk(
    idkios: int,
    uc: MasterKioskUseCase = Depends(get_usecase),
):
    master_kiosk = uc.get_by_id(idkios)
    if not master_kiosk:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MasterKiosk not found",
        )
    return master_kiosk


@router.put("/{idkios}", response_model=MasterKioskResponse)
def update_masterkiosk(
    idkios: int,
    payload: MasterKioskUpdate,
    uc: MasterKioskUseCase = Depends(get_usecase),
):
    master_kiosk = uc.update(
        idkios,
        payload.kodekiosk,
        payload.datakiosk,
        payload.level,
        payload.status,
        payload.idparent,
        payload.updated_by,
    )
    if not master_kiosk:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MasterKiosk not found",
        )
    return master_kiosk


@router.delete("/{idkios}")
def delete_masterkiosk(
    idkios: int,
    uc: MasterKioskUseCase = Depends(get_usecase),
):
    deleted = uc.delete(idkios)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MasterKiosk not found",
        )
    return {"message": "Deleted"}
