from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.infrastructure.repositories.jnsranmor_repository_impl import JnsRanmorRepositoryImpl
from app.schemas.jnsranmor_schema import JnsRanmorCreate, JnsRanmorResponse, JnsRanmorUpdate
from app.usecases.jnsranmor_usecase import JnsRanmorUseCase

router = APIRouter(prefix="/api/v1/jnsranmor", tags=["JnsRanmor"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_usecase(db: Session = Depends(get_db)):
    repo = JnsRanmorRepositoryImpl(db)
    return JnsRanmorUseCase(repo)


@router.post("/", response_model=JnsRanmorResponse)
def create_jnsranmor(
    payload: JnsRanmorCreate,
    uc: JnsRanmorUseCase = Depends(get_usecase),
):
    return uc.create(
        payload.kdranmor,
        payload.nmranmor,
        payload.snid,
        payload.status,
        payload.created_by,
        payload.updated_by,
    )


@router.get("/", response_model=list[JnsRanmorResponse])
def get_jnsranmors(uc: JnsRanmorUseCase = Depends(get_usecase)):
    return uc.get_all()


@router.get("/{kdranmor}", response_model=JnsRanmorResponse)
def get_jnsranmor(kdranmor: str, uc: JnsRanmorUseCase = Depends(get_usecase)):
    jns_ranmor = uc.get_by_id(kdranmor)
    if not jns_ranmor:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="JnsRanmor not found")
    return jns_ranmor


@router.put("/{kdranmor}", response_model=JnsRanmorResponse)
def update_jnsranmor(
    kdranmor: str,
    payload: JnsRanmorUpdate,
    uc: JnsRanmorUseCase = Depends(get_usecase),
):
    jns_ranmor = uc.update(
        kdranmor,
        payload.nmranmor,
        payload.snid,
        payload.status,
        payload.updated_by,
    )
    if not jns_ranmor:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="JnsRanmor not found")
    return jns_ranmor


@router.delete("/{kdranmor}")
def delete_jnsranmor(kdranmor: str, uc: JnsRanmorUseCase = Depends(get_usecase)):
    deleted = uc.delete(kdranmor)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="JnsRanmor not found")
    return {"message": "Deleted"}
