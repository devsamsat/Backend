from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.infrastructure.repositories.jnsprogresif_repository_impl import (
    JnsProgresifRepositoryImpl,
)
from app.schemas.jnsprogresif_schema import (
    JnsProgresifCreate,
    JnsProgresifResponse,
    JnsProgresifUpdate,
)
from app.usecases.jnsprogresif_usecase import JnsProgresifUseCase

router = APIRouter(prefix="/api/v1/jnsprogresif", tags=["JnsProgresif"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_usecase(db: Session = Depends(get_db)):
    repo = JnsProgresifRepositoryImpl(db)
    return JnsProgresifUseCase(repo)


@router.post("/", response_model=JnsProgresifResponse)
def create_jnsprogresif(
    payload: JnsProgresifCreate,
    uc: JnsProgresifUseCase = Depends(get_usecase),
):
    return uc.create(
        payload.kdprogresif,
        payload.progresifr2,
        payload.progresifr4,
        payload.created_by,
        payload.updated_by,
    )


@router.get("/", response_model=list[JnsProgresifResponse])
def get_jnsprogresifs(uc: JnsProgresifUseCase = Depends(get_usecase)):
    return uc.get_all()


@router.get("/{kdprogresif}", response_model=JnsProgresifResponse)
def get_jnsprogresif(
    kdprogresif: int,
    uc: JnsProgresifUseCase = Depends(get_usecase),
):
    jns_progresif = uc.get_by_id(kdprogresif)
    if not jns_progresif:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="JnsProgresif not found",
        )
    return jns_progresif


@router.put("/{kdprogresif}", response_model=JnsProgresifResponse)
def update_jnsprogresif(
    kdprogresif: int,
    payload: JnsProgresifUpdate,
    uc: JnsProgresifUseCase = Depends(get_usecase),
):
    jns_progresif = uc.update(
        kdprogresif,
        payload.progresifr2,
        payload.progresifr4,
        payload.updated_by,
    )
    if not jns_progresif:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="JnsProgresif not found",
        )
    return jns_progresif


@router.delete("/{kdprogresif}")
def delete_jnsprogresif(
    kdprogresif: int,
    uc: JnsProgresifUseCase = Depends(get_usecase),
):
    deleted = uc.delete(kdprogresif)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="JnsProgresif not found",
        )
    return {"message": "Deleted"}
