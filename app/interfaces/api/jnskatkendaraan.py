from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.domain.entities.jnskatkendaraan import JnsKatKendaraan
from app.infrastructure.repositories.jnskatkendaraan_repository_impl import (
    JnsKatKendaraanRepositoryImpl,
)
from app.usecases.jnskatkendaraan_usecase import JnsKatKendaraanUseCase
from app.schemas.jnskatkendaraan_schema import (
    JnsKatKendaraanCreate,
    JnsKatKendaraanResponse,
    JnsKatKendaraanUpdate,
)

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
def create_record(
    payload: JnsKatKendaraanCreate,
    uc: JnsKatKendaraanUseCase = Depends(get_usecase),
):
    entity = JnsKatKendaraan(
        katid=payload.katid,
        kendaraan=payload.kendaraan,
        jenisbpkb=payload.jenisbpkb,
        status=payload.status,
        created_by=payload.created_by,
        updated_by=payload.updated_by,
    )
    return uc.create(entity)


@router.get("/", response_model=list[JnsKatKendaraanResponse])
def get_records(uc: JnsKatKendaraanUseCase = Depends(get_usecase)):
    return uc.get_all()


@router.get("/{katid}", response_model=JnsKatKendaraanResponse)
def get_record(katid: str, uc: JnsKatKendaraanUseCase = Depends(get_usecase)):
    record = uc.get_by_id(katid)
    if not record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Record not found",
        )
    return record


@router.put("/{katid}", response_model=JnsKatKendaraanResponse)
def update_record(
    katid: str,
    payload: JnsKatKendaraanUpdate,
    uc: JnsKatKendaraanUseCase = Depends(get_usecase),
):
    entity = JnsKatKendaraan(
        katid=katid,
        kendaraan=payload.kendaraan,
        jenisbpkb=payload.jenisbpkb,
        status=payload.status,
        created_by=payload.created_by,
        updated_by=payload.updated_by,
    )
    record = uc.update(katid, entity)
    if not record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Record not found",
        )
    return record


@router.delete("/{katid}")
def delete_record(katid: str, uc: JnsKatKendaraanUseCase = Depends(get_usecase)):
    deleted = uc.delete(katid)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Record not found",
        )
    return {"message": "Deleted"}
