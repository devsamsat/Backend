from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.infrastructure.repositories.transwpdata_repository_impl import (
    TransWpDataRepositoryImpl,
)
from app.schemas.transwpdata_schema import (
    TransWpDataCreate,
    TransWpDataResponse,
    TransWpDataUpdate,
)
from app.usecases.transwpdata_usecase import TransWpDataUseCase

router = APIRouter(prefix="/api/v1/transwpdata", tags=["transwpdata"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_usecase(db: Session = Depends(get_db)):
    repo = TransWpDataRepositoryImpl(db)
    return TransWpDataUseCase(repo)


@router.post("/", response_model=TransWpDataResponse)
def create_transwpdata(
    payload: TransWpDataCreate,
    uc: TransWpDataUseCase = Depends(get_usecase),
):
    return uc.create(
        payload.idnpwpd,
        payload.kdflow,
        payload.tgldaftar,
        payload.created_by,
        payload.updated_by,
    )


@router.get("/", response_model=list[TransWpDataResponse])
def get_transwpdata(uc: TransWpDataUseCase = Depends(get_usecase)):
    return uc.get_all()


@router.get("/{idtwpdata}", response_model=TransWpDataResponse)
def get_transwpdata_by_id(
    idtwpdata: int,
    uc: TransWpDataUseCase = Depends(get_usecase),
):
    trans_wpdata = uc.get_by_id(idtwpdata)
    if not trans_wpdata:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="TransWpData not found",
        )
    return trans_wpdata


@router.put("/{idtwpdata}", response_model=TransWpDataResponse)
def update_transwpdata(
    idtwpdata: int,
    payload: TransWpDataUpdate,
    uc: TransWpDataUseCase = Depends(get_usecase),
):
    trans_wpdata = uc.update(
        idtwpdata,
        payload.idnpwpd,
        payload.kdflow,
        payload.tgldaftar,
        payload.updated_by,
    )
    if not trans_wpdata:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="TransWpData not found",
        )
    return trans_wpdata


@router.delete("/{idtwpdata}")
def delete_transwpdata(
    idtwpdata: int,
    uc: TransWpDataUseCase = Depends(get_usecase),
):
    deleted = uc.delete(idtwpdata)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="TransWpData not found",
        )
    return {"message": "Deleted"}
