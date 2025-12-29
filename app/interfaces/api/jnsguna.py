from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
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
def create_jnsguna(
    payload: JnsGunaCreate,
    uc: JnsGunaUseCase = Depends(get_usecase),
):
    return uc.create(
        payload.kdguna,
        payload.guna,
        payload.gunaplat,
        payload.progresif,
        payload.groupbpkb,
        payload.created_by,
        payload.updated_by,
    )


@router.get("/", response_model=list[JnsGunaResponse])
def get_jnsguna(uc: JnsGunaUseCase = Depends(get_usecase)):
    return uc.get_all()


@router.get("/{kdguna}", response_model=JnsGunaResponse)
def get_jnsguna_by_id(
    kdguna: str,
    uc: JnsGunaUseCase = Depends(get_usecase),
):
    record = uc.get_by_id(kdguna)
    if not record:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="JnsGuna not found")
    return record


@router.put("/{kdguna}", response_model=JnsGunaResponse)
def update_jnsguna(
    kdguna: str,
    payload: JnsGunaUpdate,
    uc: JnsGunaUseCase = Depends(get_usecase),
):
    record = uc.update(
        kdguna,
        payload.guna,
        payload.gunaplat,
        payload.progresif,
        payload.groupbpkb,
        payload.updated_by,
    )
    if not record:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="JnsGuna not found")
    return record


@router.delete("/{kdguna}")
def delete_jnsguna(
    kdguna: str,
    uc: JnsGunaUseCase = Depends(get_usecase),
):
    deleted = uc.delete(kdguna)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="JnsGuna not found")
    return {"message": "Deleted"}
