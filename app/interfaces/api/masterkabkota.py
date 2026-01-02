from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.infrastructure.repositories.masterkabkota_repository_impl import (
    MasterKabKotaRepositoryImpl,
)
from app.usecases.masterkabkota_usecase import MasterKabKotaUseCase
from app.schemas.masterkabkota_schema import (
    MasterKabKotaCreate,
    MasterKabKotaResponse,
    MasterKabKotaUpdate,
)

router = APIRouter(prefix="/api/v1/masterkabkota", tags=["masterkabkota"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_usecase(db: Session = Depends(get_db)):
    repo = MasterKabKotaRepositoryImpl(db)
    return MasterKabKotaUseCase(repo)


@router.post("/", response_model=MasterKabKotaResponse)
def create_masterkabkota(
    payload: MasterKabKotaCreate,
    uc: MasterKabKotaUseCase = Depends(get_usecase),
):
    return uc.create(
        payload.idprovinsi,
        payload.nmkabkota,
        payload.akronim,
        payload.ibukota,
        payload.status,
        payload.bpkbid,
        payload.kdkabkota,
        payload.created_by,
        payload.updated_by,
    )


@router.get("/", response_model=list[MasterKabKotaResponse])
def get_masterkabkotas(uc: MasterKabKotaUseCase = Depends(get_usecase)):
    return uc.get_all()


@router.get("/{idkabkota}", response_model=MasterKabKotaResponse)
def get_masterkabkota(
    idkabkota: int,
    uc: MasterKabKotaUseCase = Depends(get_usecase),
):
    master_kabkota = uc.get_by_id(idkabkota)
    if not master_kabkota:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MasterKabKota not found",
        )
    return master_kabkota


@router.put("/{idkabkota}", response_model=MasterKabKotaResponse)
def update_masterkabkota(
    idkabkota: int,
    payload: MasterKabKotaUpdate,
    uc: MasterKabKotaUseCase = Depends(get_usecase),
):
    master_kabkota = uc.update(
        idkabkota,
        payload.idprovinsi,
        payload.nmkabkota,
        payload.akronim,
        payload.ibukota,
        payload.status,
        payload.bpkbid,
        payload.kdkabkota,
        payload.updated_by,
    )
    if not master_kabkota:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MasterKabKota not found",
        )
    return master_kabkota


@router.delete("/{idkabkota}")
def delete_masterkabkota(
    idkabkota: int,
    uc: MasterKabKotaUseCase = Depends(get_usecase),
):
    deleted = uc.delete(idkabkota)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MasterKabKota not found",
        )
    return {"message": "Deleted"}
