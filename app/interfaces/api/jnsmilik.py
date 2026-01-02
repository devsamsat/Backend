from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.infrastructure.repositories.jnsmilik_repository_impl import JnsMilikRepositoryImpl
from app.schemas.jnsmilik_schema import JnsMilikCreate, JnsMilikResponse, JnsMilikUpdate
from app.usecases.jnsmilik_usecase import JnsMilikUseCase

router = APIRouter(prefix="/api/v1/jnsmilik", tags=["JnsMilik"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_usecase(db: Session = Depends(get_db)):
    repo = JnsMilikRepositoryImpl(db)
    return JnsMilikUseCase(repo)


@router.post("/", response_model=JnsMilikResponse)
def create_jnsmilik(payload: JnsMilikCreate, uc: JnsMilikUseCase = Depends(get_usecase)):
    return uc.create(
        payload.kdmilik,
        payload.milik,
        payload.bpkpid,
        payload.status,
        payload.created_by,
        payload.updated_by,
    )


@router.get("/", response_model=list[JnsMilikResponse])
def get_jnsmiliks(uc: JnsMilikUseCase = Depends(get_usecase)):
    return uc.get_all()


@router.get("/{kdmilik}", response_model=JnsMilikResponse)
def get_jnsmilik(kdmilik: str, uc: JnsMilikUseCase = Depends(get_usecase)):
    jns_milik = uc.get_by_id(kdmilik)
    if not jns_milik:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="JnsMilik not found")
    return jns_milik


@router.put("/{kdmilik}", response_model=JnsMilikResponse)
def update_jnsmilik(
    kdmilik: str,
    payload: JnsMilikUpdate,
    uc: JnsMilikUseCase = Depends(get_usecase),
):
    jns_milik = uc.update(
        kdmilik,
        payload.milik,
        payload.bpkpid,
        payload.status,
        payload.updated_by,
    )
    if not jns_milik:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="JnsMilik not found")
    return jns_milik


@router.delete("/{kdmilik}")
def delete_jnsmilik(kdmilik: str, uc: JnsMilikUseCase = Depends(get_usecase)):
    deleted = uc.delete(kdmilik)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="JnsMilik not found")
    return {"message": "Deleted"}
