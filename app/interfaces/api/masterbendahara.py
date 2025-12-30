from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.infrastructure.repositories.masterbendahara_repository_impl import (
    MasterBendaharaRepositoryImpl,
)
from app.usecases.masterbendahara_usecase import MasterBendaharaUseCase
from app.schemas.masterbendahara_schema import (
    MasterBendaharaCreate,
    MasterBendaharaResponse,
    MasterBendaharaUpdate,
)

router = APIRouter(prefix="/api/v1/masterbendahara", tags=["masterbendahara"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_usecase(db: Session = Depends(get_db)):
    repo = MasterBendaharaRepositoryImpl(db)
    return MasterBendaharaUseCase(repo)


@router.post("/", response_model=MasterBendaharaResponse)
def create_masterbendahara(
    payload: MasterBendaharaCreate,
    uc: MasterBendaharaUseCase = Depends(get_usecase),
):
    return uc.create(
        payload.idpegawai,
        payload.idbank,
        payload.norek,
        payload.namarek,
        payload.jnsbend,
        payload.status,
        payload.jabatan,
        payload.pangkat,
        payload.uid,
        payload.koordinator,
        payload.idreknrc,
        payload.telepon,
        payload.ket,
        payload.created_by,
        payload.updated_by,
    )


@router.get("/", response_model=list[MasterBendaharaResponse])
def get_masterbendaharas(uc: MasterBendaharaUseCase = Depends(get_usecase)):
    return uc.get_all()


@router.get("/{idbend}", response_model=MasterBendaharaResponse)
def get_masterbendahara(idbend: int, uc: MasterBendaharaUseCase = Depends(get_usecase)):
    master_bendahara = uc.get_by_id(idbend)
    if not master_bendahara:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MasterBendahara not found",
        )
    return master_bendahara


@router.put("/{idbend}", response_model=MasterBendaharaResponse)
def update_masterbendahara(
    idbend: int,
    payload: MasterBendaharaUpdate,
    uc: MasterBendaharaUseCase = Depends(get_usecase),
):
    master_bendahara = uc.update(
        idbend,
        payload.idpegawai,
        payload.idbank,
        payload.norek,
        payload.namarek,
        payload.jnsbend,
        payload.status,
        payload.jabatan,
        payload.pangkat,
        payload.uid,
        payload.koordinator,
        payload.idreknrc,
        payload.telepon,
        payload.ket,
        payload.updated_by,
    )
    if not master_bendahara:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MasterBendahara not found",
        )
    return master_bendahara


@router.delete("/{idbend}")
def delete_masterbendahara(idbend: int, uc: MasterBendaharaUseCase = Depends(get_usecase)):
    deleted = uc.delete(idbend)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MasterBendahara not found",
        )
    return {"message": "Deleted"}
