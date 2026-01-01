from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.infrastructure.repositories.jnsgolongan_repository_impl import JnsGolonganRepositoryImpl
from app.usecases.jnsgolongan_usecase import JnsGolonganUseCase
from app.schemas.jnsgolongan_schema import (
    JnsGolonganCreate,
    JnsGolonganResponse,
    JnsGolonganUpdate,
)

router = APIRouter(prefix="/api/v1/jnsgolongan", tags=["JnsGolongan"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_usecase(db: Session = Depends(get_db)):
    repo = JnsGolonganRepositoryImpl(db)
    return JnsGolonganUseCase(repo)


@router.post("/", response_model=JnsGolonganResponse)
def create_jnsgolongan(
    payload: JnsGolonganCreate,
    uc: JnsGolonganUseCase = Depends(get_usecase),
):
    return uc.create(
        payload.jnsgolid,
        payload.golongan,
        payload.katid,
        payload.jnskendid,
        payload.viewall,
        payload.status,
        payload.created_by,
        payload.updated_by,
    )


@router.get("/", response_model=list[JnsGolonganResponse])
def get_jnsgolongan(uc: JnsGolonganUseCase = Depends(get_usecase)):
    return uc.get_all()


@router.get("/{jnsgolid}", response_model=JnsGolonganResponse)
def get_jnsgolongan_by_id(
    jnsgolid: str,
    uc: JnsGolonganUseCase = Depends(get_usecase),
):
    record = uc.get_by_id(jnsgolid)
    if not record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="JnsGolongan not found",
        )
    return record


@router.put("/{jnsgolid}", response_model=JnsGolonganResponse)
def update_jnsgolongan(
    jnsgolid: str,
    payload: JnsGolonganUpdate,
    uc: JnsGolonganUseCase = Depends(get_usecase),
):
    record = uc.update(
        jnsgolid,
        payload.golongan,
        payload.katid,
        payload.jnskendid,
        payload.viewall,
        payload.status,
        payload.updated_by,
    )
    if not record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="JnsGolongan not found",
        )
    return record


@router.delete("/{jnsgolid}")
def delete_jnsgolongan(
    jnsgolid: str,
    uc: JnsGolonganUseCase = Depends(get_usecase),
):
    deleted = uc.delete(jnsgolid)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="JnsGolongan not found",
        )
    return {"message": "Deleted"}
