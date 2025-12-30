from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.domain.entities.jnsguna import JnsGuna
from app.infrastructure.repositories.jnsguna_repository_impl import JnsGunaRepositoryImpl
from app.usecases.jnsguna_usecase import JnsGunaUseCase
from app.schemas.jnsguna_schema import JnsGunaCreate, JnsGunaResponse, JnsGunaUpdate

router = APIRouter(prefix="/api/v1/jnsguna", tags=["JnsGuna"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_usecase(db: Session = Depends(get_db)):
    repo = JnsGunaRepositoryImpl(db)
    return JnsGunaUseCase(repo)


@router.post("/", response_model=JnsGunaResponse)
def create_record(payload: JnsGunaCreate, uc: JnsGunaUseCase = Depends(get_usecase)):
    entity = JnsGuna(
        kdguna=payload.kdguna,
        guna=payload.guna,
        gunaplat=payload.gunaplat,
        progresif=payload.progresif,
        groupbpkb=payload.groupbpkb,
        created_by=payload.created_by,
        updated_by=payload.updated_by,
    )
    return uc.create(entity)


@router.get("/", response_model=list[JnsGunaResponse])
def get_records(uc: JnsGunaUseCase = Depends(get_usecase)):
    return uc.get_all()


@router.get("/{kdguna}", response_model=JnsGunaResponse)
def get_record(kdguna: str, uc: JnsGunaUseCase = Depends(get_usecase)):
    record = uc.get_by_id(kdguna)
    if not record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Record not found",
        )
    return record


@router.put("/{kdguna}", response_model=JnsGunaResponse)
def update_record(
    kdguna: str,
    payload: JnsGunaUpdate,
    uc: JnsGunaUseCase = Depends(get_usecase),
):
    entity = JnsGuna(
        kdguna=kdguna,
        guna=payload.guna,
        gunaplat=payload.gunaplat,
        progresif=payload.progresif,
        groupbpkb=payload.groupbpkb,
        created_by=payload.created_by,
        updated_by=payload.updated_by,
    )
    record = uc.update(kdguna, entity)
    if not record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Record not found",
        )
    return record


@router.delete("/{kdguna}")
def delete_record(kdguna: str, uc: JnsGunaUseCase = Depends(get_usecase)):
    deleted = uc.delete(kdguna)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Record not found",
        )
    return {"message": "Deleted"}
