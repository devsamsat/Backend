from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.infrastructure.repositories.masteruunjop_repository_impl import (
    MasterUunJopRepositoryImpl,
)
from app.usecases.masteruunjop_usecase import MasterUunJopUseCase
from app.schemas.masteruunjop_schema import (
    MasterUunJopCreate,
    MasterUunJopResponse,
    MasterUunJopUpdate,
)

router = APIRouter(prefix="/api/v1/masteruunjop", tags=["masteruunjop"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_usecase(db: Session = Depends(get_db)):
    repo = MasterUunJopRepositoryImpl(db)
    return MasterUunJopUseCase(repo)


@router.post("/", response_model=MasterUunJopResponse)
def create_masteruunjop(
    payload: MasterUunJopCreate,
    uc: MasterUunJopUseCase = Depends(get_usecase),
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


@router.get("/", response_model=list[MasterUunJopResponse])
def get_masteruunjops(uc: MasterUunJopUseCase = Depends(get_usecase)):
    return uc.get_all()


@router.get("/{iduunjop}", response_model=MasterUunJopResponse)
def get_masteruunjop(
    iduunjop: int,
    uc: MasterUunJopUseCase = Depends(get_usecase),
):
    master_uun_jop = uc.get_by_id(iduunjop)
    if not master_uun_jop:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MasterUunJop not found",
        )
    return master_uun_jop


@router.put("/{iduunjop}", response_model=MasterUunJopResponse)
def update_masteruunjop(
    iduunjop: int,
    payload: MasterUunJopUpdate,
    uc: MasterUunJopUseCase = Depends(get_usecase),
):
    master_uun_jop = uc.update(
        iduunjop,
        payload.noperkada,
        payload.isiperkada,
        payload.tahun,
        payload.status,
        payload.keterangan,
        payload.updated_by,
    )
    if not master_uun_jop:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MasterUunJop not found",
        )
    return master_uun_jop


@router.delete("/{iduunjop}")
def delete_masteruunjop(
    iduunjop: int,
    uc: MasterUunJopUseCase = Depends(get_usecase),
):
    deleted = uc.delete(iduunjop)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MasterUunJop not found",
        )
    return {"message": "Deleted"}
