from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.infrastructure.repositories.jnskendaraan_repository_impl import (
    JnsKendaraanRepositoryImpl,
)
from app.schemas.jnskendaraan_schema import (
    JnsKendaraanCreate,
    JnsKendaraanResponse,
    JnsKendaraanUpdate,
)
from app.usecases.jnskendaraan_usecase import JnsKendaraanUseCase

router = APIRouter(prefix="/api/v1/jnskendaraan", tags=["JnsKendaraan"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_usecase(db: Session = Depends(get_db)):
    repo = JnsKendaraanRepositoryImpl(db)
    return JnsKendaraanUseCase(repo)


@router.post("/", response_model=JnsKendaraanResponse)
def create_jnskendaraan(
    payload: JnsKendaraanCreate,
    uc: JnsKendaraanUseCase = Depends(get_usecase),
):
    return uc.create(
        payload.jnskendid,
        payload.jnskend,
        payload.katid,
        payload.jnsjrid,
        payload.golpjr,
        payload.golujr,
        payload.created_by,
        payload.updated_by,
    )


@router.get("/", response_model=list[JnsKendaraanResponse])
def get_jnskendaraans(uc: JnsKendaraanUseCase = Depends(get_usecase)):
    return uc.get_all()


@router.get("/{jnskendid}", response_model=JnsKendaraanResponse)
def get_jnskendaraan(jnskendid: str, uc: JnsKendaraanUseCase = Depends(get_usecase)):
    jns_kendaraan = uc.get_by_id(jnskendid)
    if not jns_kendaraan:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="JnsKendaraan not found",
        )
    return jns_kendaraan


@router.put("/{jnskendid}", response_model=JnsKendaraanResponse)
def update_jnskendaraan(
    jnskendid: str,
    payload: JnsKendaraanUpdate,
    uc: JnsKendaraanUseCase = Depends(get_usecase),
):
    jns_kendaraan = uc.update(
        jnskendid,
        payload.jnskend,
        payload.katid,
        payload.jnsjrid,
        payload.golpjr,
        payload.golujr,
        payload.updated_by,
    )
    if not jns_kendaraan:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="JnsKendaraan not found",
        )
    return jns_kendaraan


@router.delete("/{jnskendid}")
def delete_jnskendaraan(
    jnskendid: str,
    uc: JnsKendaraanUseCase = Depends(get_usecase),
):
    deleted = uc.delete(jnskendid)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="JnsKendaraan not found",
        )
    return {"message": "Deleted"}
