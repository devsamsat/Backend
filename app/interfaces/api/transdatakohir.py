from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.infrastructure.repositories.transdatakohir_repository_impl import (
    TransDataKohirRepositoryImpl,
)
from app.usecases.transdatakohir_usecase import TransDataKohirUseCase
from app.schemas.transdatakohir_schema import (
    TransDataKohirCreate,
    TransDataKohirResponse,
    TransDataKohirUpdate,
)

router = APIRouter(prefix="/api/v1/transdatakohir", tags=["transdatakohir"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_usecase(db: Session = Depends(get_db)):
    repo = TransDataKohirRepositoryImpl(db)
    return TransDataKohirUseCase(repo)


@router.post("/", response_model=TransDataKohirResponse)
def create_transdatakohir(
    payload: TransDataKohirCreate,
    uc: TransDataKohirUseCase = Depends(get_usecase),
):
    return uc.create(
        payload.penagih,
        payload.idwp,
        payload.masaawal,
        payload.masaakhir,
        payload.tglpenetapan,
        payload.tglkurangbayar,
        payload.keterangan,
        payload.idupt,
        payload.skrupt,
        payload.validjr,
        payload.validjrby,
        payload.validpol,
        payload.validpolby,
        payload.ntpd,
        payload.tglntpd,
        payload.idbank,
        payload.created_by,
        payload.updated_by,
    )


@router.get("/", response_model=list[TransDataKohirResponse])
def get_transdatakohir(uc: TransDataKohirUseCase = Depends(get_usecase)):
    return uc.get_all()


@router.get("/{idkohir}", response_model=TransDataKohirResponse)
def get_transdatakohir_by_id(
    idkohir: int,
    uc: TransDataKohirUseCase = Depends(get_usecase),
):
    trans_data_kohir = uc.get_by_id(idkohir)
    if not trans_data_kohir:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="TransDataKohir not found",
        )
    return trans_data_kohir


@router.put("/{idkohir}", response_model=TransDataKohirResponse)
def update_transdatakohir(
    idkohir: int,
    payload: TransDataKohirUpdate,
    uc: TransDataKohirUseCase = Depends(get_usecase),
):
    trans_data_kohir = uc.update(
        idkohir,
        payload.penagih,
        payload.idwp,
        payload.masaawal,
        payload.masaakhir,
        payload.tglpenetapan,
        payload.tglkurangbayar,
        payload.keterangan,
        payload.idupt,
        payload.skrupt,
        payload.validjr,
        payload.validjrby,
        payload.validpol,
        payload.validpolby,
        payload.ntpd,
        payload.tglntpd,
        payload.idbank,
        payload.updated_by,
    )
    if not trans_data_kohir:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="TransDataKohir not found",
        )
    return trans_data_kohir


@router.delete("/{idkohir}")
def delete_transdatakohir(
    idkohir: int,
    uc: TransDataKohirUseCase = Depends(get_usecase),
):
    deleted = uc.delete(idkohir)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="TransDataKohir not found",
        )
    return {"message": "Deleted"}
