from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.infrastructure.repositories.jnsstrurek_repository_impl import JnsStruRekRepositoryImpl
from app.schemas.jnsstrurek_schema import (
    JnsStruRekCreate,
    JnsStruRekResponse,
    JnsStruRekUpdate,
)
from app.usecases.jnsstrurek_usecase import JnsStruRekUseCase

router = APIRouter(prefix="/api/v1/jnsstrurek", tags=["jnsstrurek"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_usecase(db: Session = Depends(get_db)):
    repo = JnsStruRekRepositoryImpl(db)
    return JnsStruRekUseCase(repo)


@router.post("/", response_model=JnsStruRekResponse)
def create_jnsstrurek(
    payload: JnsStruRekCreate,
    uc: JnsStruRekUseCase = Depends(get_usecase),
):
    return uc.create(
        payload.mtglevel,
        payload.nmlevel,
        payload.keterangan,
        payload.created_by,
        payload.updated_by,
    )


@router.get("/", response_model=list[JnsStruRekResponse])
def get_jnsstrureks(uc: JnsStruRekUseCase = Depends(get_usecase)):
    return uc.get_all()


@router.get("/{mtglevel}", response_model=JnsStruRekResponse)
def get_jnsstrurek(mtglevel: str, uc: JnsStruRekUseCase = Depends(get_usecase)):
    record = uc.get_by_id(mtglevel)
    if not record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="JnsStruRek not found",
        )
    return record


@router.put("/{mtglevel}", response_model=JnsStruRekResponse)
def update_jnsstrurek(
    mtglevel: str,
    payload: JnsStruRekUpdate,
    uc: JnsStruRekUseCase = Depends(get_usecase),
):
    record = uc.update(
        mtglevel,
        payload.nmlevel,
        payload.keterangan,
        payload.updated_by,
    )
    if not record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="JnsStruRek not found",
        )
    return record


@router.delete("/{mtglevel}")
def delete_jnsstrurek(mtglevel: str, uc: JnsStruRekUseCase = Depends(get_usecase)):
    deleted = uc.delete(mtglevel)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="JnsStruRek not found",
        )
    return {"message": "Deleted"}
