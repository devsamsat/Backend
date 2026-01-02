from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.infrastructure.repositories.transwpdatafile_repository_impl import (
    TransWpDataFileRepositoryImpl,
)
from app.schemas.transwpdatafile_schema import (
    TransWpDataFileCreate,
    TransWpDataFileResponse,
    TransWpDataFileUpdate,
)
from app.usecases.transwpdatafile_usecase import TransWpDataFileUseCase

router = APIRouter(prefix="/api/v1/transwpdatafile", tags=["transwpdatafile"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_usecase(db: Session = Depends(get_db)):
    repo = TransWpDataFileRepositoryImpl(db)
    return TransWpDataFileUseCase(repo)


@router.post("/", response_model=TransWpDataFileResponse)
def create_transwpdatafile(
    payload: TransWpDataFileCreate,
    uc: TransWpDataFileUseCase = Depends(get_usecase),
):
    return uc.create(
        payload.idtwpdata,
        payload.namafile,
        payload.direktory,
        payload.extension,
        payload.size,
        payload.url,
        payload.created_by,
        payload.updated_by,
    )


@router.get("/", response_model=list[TransWpDataFileResponse])
def get_transwpdatafile(
    uc: TransWpDataFileUseCase = Depends(get_usecase),
):
    return uc.get_all()


@router.get("/{idfile}", response_model=TransWpDataFileResponse)
def get_transwpdatafile_by_id(
    idfile: int,
    uc: TransWpDataFileUseCase = Depends(get_usecase),
):
    trans_wpdatafile = uc.get_by_id(idfile)
    if not trans_wpdatafile:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="TransWpDataFile not found",
        )
    return trans_wpdatafile


@router.put("/{idfile}", response_model=TransWpDataFileResponse)
def update_transwpdatafile(
    idfile: int,
    payload: TransWpDataFileUpdate,
    uc: TransWpDataFileUseCase = Depends(get_usecase),
):
    trans_wpdatafile = uc.update(
        idfile,
        payload.idtwpdata,
        payload.namafile,
        payload.direktory,
        payload.extension,
        payload.size,
        payload.url,
        payload.updated_by,
    )
    if not trans_wpdatafile:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="TransWpDataFile not found",
        )
    return trans_wpdatafile


@router.delete("/{idfile}")
def delete_transwpdatafile(
    idfile: int,
    uc: TransWpDataFileUseCase = Depends(get_usecase),
):
    deleted = uc.delete(idfile)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="TransWpDataFile not found",
        )
    return {"message": "Deleted"}
