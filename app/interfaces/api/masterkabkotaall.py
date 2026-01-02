from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.infrastructure.repositories.masterkabkotaall_repository_impl import (
    MasterKabKotaAllRepositoryImpl,
)
from app.usecases.masterkabkotaall_usecase import MasterKabKotaAllUseCase
from app.schemas.masterkabkotaall_schema import (
    MasterKabKotaAllCreate,
    MasterKabKotaAllResponse,
    MasterKabKotaAllUpdate,
)

router = APIRouter(prefix="/api/v1/masterkabkotaall", tags=["masterkabkotaall"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_usecase(db: Session = Depends(get_db)):
    repo = MasterKabKotaAllRepositoryImpl(db)
    return MasterKabKotaAllUseCase(repo)


@router.post("/", response_model=MasterKabKotaAllResponse)
def create_masterkabkotaall(
    payload: MasterKabKotaAllCreate,
    uc: MasterKabKotaAllUseCase = Depends(get_usecase),
):
    return uc.create(
        payload.idprovinsi,
        payload.nmkabkota,
        payload.status,
        payload.kdkabkota,
        payload.created_by,
        payload.updated_by,
    )


@router.get("/", response_model=list[MasterKabKotaAllResponse])
def get_masterkabkotaalls(uc: MasterKabKotaAllUseCase = Depends(get_usecase)):
    return uc.get_all()


@router.get("/{idkabkotaall}", response_model=MasterKabKotaAllResponse)
def get_masterkabkotaall(
    idkabkotaall: int,
    uc: MasterKabKotaAllUseCase = Depends(get_usecase),
):
    master_kabkotaall = uc.get_by_id(idkabkotaall)
    if not master_kabkotaall:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MasterKabKotaAll not found",
        )
    return master_kabkotaall


@router.put("/{idkabkotaall}", response_model=MasterKabKotaAllResponse)
def update_masterkabkotaall(
    idkabkotaall: int,
    payload: MasterKabKotaAllUpdate,
    uc: MasterKabKotaAllUseCase = Depends(get_usecase),
):
    master_kabkotaall = uc.update(
        idkabkotaall,
        payload.idprovinsi,
        payload.nmkabkota,
        payload.status,
        payload.kdkabkota,
        payload.updated_by,
    )
    if not master_kabkotaall:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MasterKabKotaAll not found",
        )
    return master_kabkotaall


@router.delete("/{idkabkotaall}")
def delete_masterkabkotaall(
    idkabkotaall: int,
    uc: MasterKabKotaAllUseCase = Depends(get_usecase),
):
    deleted = uc.delete(idkabkotaall)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MasterKabKotaAll not found",
        )
    return {"message": "Deleted"}
