from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.infrastructure.repositories.masteruunjop_repository_impl import (
    MasterUuNjopRepositoryImpl,
)
from app.usecases.masteruunjop_usecase import MasterUuNjopUseCase
from app.schemas.masteruunjop_schema import (
    MasterUuNjopCreate,
    MasterUuNjopResponse,
    MasterUuNjopUpdate,
)

router = APIRouter(prefix="/api/v1/masteruunjop", tags=["MasterUuNjop"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_usecase(db: Session = Depends(get_db)):
    repo = MasterUuNjopRepositoryImpl(db)
    return MasterUuNjopUseCase(repo)


@router.post("/", response_model=MasterUuNjopResponse)
def create_masteruunjop(
    payload: MasterUuNjopCreate,
    uc: MasterUuNjopUseCase = Depends(get_usecase),
):
    return uc.create(
        payload.noperkada,
        payload.isiperkada,
        payload.tahun,
        payload.status,
        payload.keterangan,
        payload.created_by,
        payload.updated_by,
    )


@router.get("/", response_model=list[MasterUuNjopResponse])
def get_masteruunjops(uc: MasterUuNjopUseCase = Depends(get_usecase)):
    return uc.get_all()


@router.get("/{iduunjop}", response_model=MasterUuNjopResponse)
def get_masteruunjop(
    iduunjop: int,
    uc: MasterUuNjopUseCase = Depends(get_usecase),
):
    record = uc.get_by_id(iduunjop)
    if not record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MasterUuNjop not found",
        )
    return record


@router.put("/{iduunjop}", response_model=MasterUuNjopResponse)
def update_masteruunjop(
    iduunjop: int,
    payload: MasterUuNjopUpdate,
    uc: MasterUuNjopUseCase = Depends(get_usecase),
):
    record = uc.update(
        iduunjop,
        payload.noperkada,
        payload.isiperkada,
        payload.tahun,
        payload.status,
        payload.keterangan,
        payload.updated_by,
    )
    if not record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MasterUuNjop not found",
        )
    return record


@router.delete("/{iduunjop}")
def delete_masteruunjop(
    iduunjop: int,
    uc: MasterUuNjopUseCase = Depends(get_usecase),
):
    deleted = uc.delete(iduunjop)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MasterUuNjop not found",
        )
    return {"message": "Deleted"}
