from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.infrastructure.repositories.jnskatkendaraan_repository_impl import (
    JnsKatKendaraanRepositoryImpl,
)
from app.schemas.jnskatkendaraan_schema import (
    JnsKatKendaraanCreate,
    JnsKatKendaraanResponse,
    JnsKatKendaraanUpdate,
)
from app.usecases.jnskatkendaraan_usecase import JnsKatKendaraanUseCase

router = APIRouter(prefix="/api/v1/jnskatkendaraan", tags=["JnsKatKendaraan"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_usecase(db: Session = Depends(get_db)):
    repo = JnsKatKendaraanRepositoryImpl(db)
    return JnsKatKendaraanUseCase(repo)


@router.post("/", response_model=JnsKatKendaraanResponse)
def create_jnskatkendaraan(
    payload: JnsKatKendaraanCreate,
    uc: JnsKatKendaraanUseCase = Depends(get_usecase),
):
    return uc.create(
        payload.katid,
        payload.kendaraan,
        payload.jenisbpkb,
        payload.status,
        payload.created_by,
        payload.updated_by,
    )


@router.get("/", response_model=list[JnsKatKendaraanResponse])
def get_jnskatkendaraans(uc: JnsKatKendaraanUseCase = Depends(get_usecase)):
    return uc.get_all()


@router.get("/{katid}", response_model=JnsKatKendaraanResponse)
def get_jnskatkendaraan(
    katid: str,
    uc: JnsKatKendaraanUseCase = Depends(get_usecase),
):
    jns_katkendaraan = uc.get_by_id(katid)
    if not jns_katkendaraan:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="JnsKatKendaraan not found",
        )
    return jns_katkendaraan


@router.put("/{katid}", response_model=JnsKatKendaraanResponse)
def update_jnskatkendaraan(
    katid: str,
    payload: JnsKatKendaraanUpdate,
    uc: JnsKatKendaraanUseCase = Depends(get_usecase),
):
    jns_katkendaraan = uc.update(
        katid,
        payload.kendaraan,
        payload.jenisbpkb,
        payload.status,
        payload.updated_by,
    )
    if not jns_katkendaraan:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="JnsKatKendaraan not found",
        )
    return jns_katkendaraan


@router.delete("/{katid}")
def delete_jnskatkendaraan(
    katid: str,
    uc: JnsKatKendaraanUseCase = Depends(get_usecase),
):
    deleted = uc.delete(katid)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="JnsKatKendaraan not found",
        )
    return {"message": "Deleted"}
