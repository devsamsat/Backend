from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.infrastructure.repositories.masterreknrc_repository_impl import (
    MasterRekNrcRepositoryImpl,
)
from app.usecases.masterreknrc_usecase import MasterRekNrcUseCase
from app.schemas.masterreknrc_schema import (
    MasterRekNrcCreate,
    MasterRekNrcResponse,
    MasterRekNrcUpdate,
)

router = APIRouter(prefix="/api/v1/masterreknrc", tags=["masterreknrc"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_usecase(db: Session = Depends(get_db)):
    repo = MasterRekNrcRepositoryImpl(db)
    return MasterRekNrcUseCase(repo)


@router.post("/", response_model=MasterRekNrcResponse)
def create_masterreknrc(
    payload: MasterRekNrcCreate,
    uc: MasterRekNrcUseCase = Depends(get_usecase),
):
    return uc.create(
        payload.kdrek,
        payload.mtglevel,
        payload.nmrek,
        payload.rek_type,
        payload.created_by,
        payload.updated_by,
    )


@router.get("/", response_model=list[MasterRekNrcResponse])
def get_masterreknrcs(uc: MasterRekNrcUseCase = Depends(get_usecase)):
    return uc.get_all()


@router.get("/{idreknrc}", response_model=MasterRekNrcResponse)
def get_masterreknrc(idreknrc: int, uc: MasterRekNrcUseCase = Depends(get_usecase)):
    master_reknrc = uc.get_by_id(idreknrc)
    if not master_reknrc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MasterRekNrc not found",
        )
    return master_reknrc


@router.put("/{idreknrc}", response_model=MasterRekNrcResponse)
def update_masterreknrc(
    idreknrc: int,
    payload: MasterRekNrcUpdate,
    uc: MasterRekNrcUseCase = Depends(get_usecase),
):
    master_reknrc = uc.update(
        idreknrc,
        payload.kdrek,
        payload.mtglevel,
        payload.nmrek,
        payload.rek_type,
        payload.updated_by,
    )
    if not master_reknrc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MasterRekNrc not found",
        )
    return master_reknrc


@router.delete("/{idreknrc}")
def delete_masterreknrc(
    idreknrc: int,
    uc: MasterRekNrcUseCase = Depends(get_usecase),
):
    deleted = uc.delete(idreknrc)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MasterRekNrc not found",
        )
    return {"message": "Deleted"}
