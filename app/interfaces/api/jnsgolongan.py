from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.domain.entities.jnsgolongan import JnsGolongan
from app.infrastructure.repositories.jnsgolongan_repository_impl import (
    JnsGolonganRepositoryImpl,
)
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
def create_record(
    payload: JnsGolonganCreate,
    uc: JnsGolonganUseCase = Depends(get_usecase),
):
    entity = JnsGolongan(
        jnsgolid=payload.jnsgolid,
        golongan=payload.golongan,
        katid=payload.katid,
        jnskendid=payload.jnskendid,
        viewall=payload.viewall,
        status=payload.status,
        created_by=payload.created_by,
        updated_by=payload.updated_by,
    )
    return uc.create(entity)


@router.get("/", response_model=list[JnsGolonganResponse])
def get_records(uc: JnsGolonganUseCase = Depends(get_usecase)):
    return uc.get_all()


@router.get("/{jnsgolid}", response_model=JnsGolonganResponse)
def get_record(jnsgolid: str, uc: JnsGolonganUseCase = Depends(get_usecase)):
    record = uc.get_by_id(jnsgolid)
    if not record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Record not found",
        )
    return record


@router.put("/{jnsgolid}", response_model=JnsGolonganResponse)
def update_record(
    jnsgolid: str,
    payload: JnsGolonganUpdate,
    uc: JnsGolonganUseCase = Depends(get_usecase),
):
    entity = JnsGolongan(
        jnsgolid=jnsgolid,
        golongan=payload.golongan,
        katid=payload.katid,
        jnskendid=payload.jnskendid,
        viewall=payload.viewall,
        status=payload.status,
        created_by=payload.created_by,
        updated_by=payload.updated_by,
    )
    record = uc.update(jnsgolid, entity)
    if not record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Record not found",
        )
    return record


@router.delete("/{jnsgolid}")
def delete_record(jnsgolid: str, uc: JnsGolonganUseCase = Depends(get_usecase)):
    deleted = uc.delete(jnsgolid)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Record not found",
        )
    return {"message": "Deleted"}
