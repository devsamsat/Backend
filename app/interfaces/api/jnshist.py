from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.infrastructure.repositories.jnshist_repository_impl import JnsHistRepositoryImpl
from app.schemas.jnshist_schema import JnsHistCreate, JnsHistResponse, JnsHistUpdate
from app.usecases.jnshist_usecase import JnsHistUseCase

router = APIRouter(prefix="/api/v1/jnshist", tags=["JnsHist"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_usecase(db: Session = Depends(get_db)):
    repo = JnsHistRepositoryImpl(db)
    return JnsHistUseCase(repo)


@router.post("/", response_model=JnsHistResponse)
def create_jnshist(payload: JnsHistCreate, uc: JnsHistUseCase = Depends(get_usecase)):
    return uc.create(
        payload.kdhist,
        payload.nmhist,
        payload.kdflow,
        payload.status,
        payload.created_by,
        payload.updated_by,
    )


@router.get("/", response_model=list[JnsHistResponse])
def get_jnshists(uc: JnsHistUseCase = Depends(get_usecase)):
    return uc.get_all()


@router.get("/{kdhist}", response_model=JnsHistResponse)
def get_jnshist(kdhist: str, uc: JnsHistUseCase = Depends(get_usecase)):
    jns_hist = uc.get_by_id(kdhist)
    if not jns_hist:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="JnsHist not found")
    return jns_hist


@router.put("/{kdhist}", response_model=JnsHistResponse)
def update_jnshist(
    kdhist: str,
    payload: JnsHistUpdate,
    uc: JnsHistUseCase = Depends(get_usecase),
):
    jns_hist = uc.update(
        kdhist,
        payload.nmhist,
        payload.kdflow,
        payload.status,
        payload.updated_by,
    )
    if not jns_hist:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="JnsHist not found")
    return jns_hist


@router.delete("/{kdhist}")
def delete_jnshist(kdhist: str, uc: JnsHistUseCase = Depends(get_usecase)):
    deleted = uc.delete(kdhist)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="JnsHist not found")
    return {"message": "Deleted"}
