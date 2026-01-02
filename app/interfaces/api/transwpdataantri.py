from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.infrastructure.repositories.transwpdataantri_repository_impl import (
    TransWpDataAntriRepositoryImpl,
)
from app.schemas.transwpdataantri_schema import (
    TransWpDataAntriCreate,
    TransWpDataAntriResponse,
    TransWpDataAntriUpdate,
)
from app.usecases.transwpdataantri_usecase import TransWpDataAntriUseCase

router = APIRouter(prefix="/api/v1/transwpdataantri", tags=["transwpdataantri"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_usecase(db: Session = Depends(get_db)):
    repo = TransWpDataAntriRepositoryImpl(db)
    return TransWpDataAntriUseCase(repo)


@router.post("/", response_model=TransWpDataAntriResponse)
def create_transwpdataantri(
    payload: TransWpDataAntriCreate,
    uc: TransWpDataAntriUseCase = Depends(get_usecase),
):
    return uc.create(
        payload.idtwpdata,
        payload.noantri,
        payload.idktp,
        payload.statantri,
        payload.ket,
        payload.tglantri,
        payload.created_by,
        payload.updated_by,
    )


@router.get("/", response_model=list[TransWpDataAntriResponse])
def get_transwpdataantri(
    uc: TransWpDataAntriUseCase = Depends(get_usecase),
):
    return uc.get_all()


@router.get("/{idantri}", response_model=TransWpDataAntriResponse)
def get_transwpdataantri_by_id(
    idantri: int,
    uc: TransWpDataAntriUseCase = Depends(get_usecase),
):
    trans_wpdataantri = uc.get_by_id(idantri)
    if not trans_wpdataantri:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="TransWpDataAntri not found",
        )
    return trans_wpdataantri


@router.put("/{idantri}", response_model=TransWpDataAntriResponse)
def update_transwpdataantri(
    idantri: int,
    payload: TransWpDataAntriUpdate,
    uc: TransWpDataAntriUseCase = Depends(get_usecase),
):
    trans_wpdataantri = uc.update(
        idantri,
        payload.idtwpdata,
        payload.noantri,
        payload.idktp,
        payload.statantri,
        payload.ket,
        payload.tglantri,
        payload.updated_by,
    )
    if not trans_wpdataantri:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="TransWpDataAntri not found",
        )
    return trans_wpdataantri


@router.delete("/{idantri}")
def delete_transwpdataantri(
    idantri: int,
    uc: TransWpDataAntriUseCase = Depends(get_usecase),
):
    deleted = uc.delete(idantri)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="TransWpDataAntri not found",
        )
    return {"message": "Deleted"}
