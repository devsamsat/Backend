from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.infrastructure.repositories.jnsjr_repository_impl import JnsJrRepositoryImpl
from app.schemas.jnsjr_schema import JnsJrCreate, JnsJrResponse, JnsJrUpdate
from app.usecases.jnsjr_usecase import JnsJrUseCase

router = APIRouter(prefix="/api/v1/jnsjr", tags=["JnsJr"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_usecase(db: Session = Depends(get_db)):
    repo = JnsJrRepositoryImpl(db)
    return JnsJrUseCase(repo)


@router.post("/", response_model=JnsJrResponse)
def create_jnsjr(payload: JnsJrCreate, uc: JnsJrUseCase = Depends(get_usecase)):
    return uc.create(
        payload.jnsjrid,
        payload.kodejr,
        payload.goljns,
        payload.pu,
        payload.roda,
        payload.keterangan,
        payload.created_by,
        payload.updated_by,
    )


@router.get("/", response_model=list[JnsJrResponse])
def get_jnsjrs(uc: JnsJrUseCase = Depends(get_usecase)):
    return uc.get_all()


@router.get("/{jnsjrid}", response_model=JnsJrResponse)
def get_jnsjr(jnsjrid: str, uc: JnsJrUseCase = Depends(get_usecase)):
    jns_jr = uc.get_by_id(jnsjrid)
    if not jns_jr:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="JnsJr not found")
    return jns_jr


@router.put("/{jnsjrid}", response_model=JnsJrResponse)
def update_jnsjr(
    jnsjrid: str,
    payload: JnsJrUpdate,
    uc: JnsJrUseCase = Depends(get_usecase),
):
    jns_jr = uc.update(
        jnsjrid,
        payload.kodejr,
        payload.goljns,
        payload.pu,
        payload.roda,
        payload.keterangan,
        payload.updated_by,
    )
    if not jns_jr:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="JnsJr not found")
    return jns_jr


@router.delete("/{jnsjrid}")
def delete_jnsjr(jnsjrid: str, uc: JnsJrUseCase = Depends(get_usecase)):
    deleted = uc.delete(jnsjrid)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="JnsJr not found")
    return {"message": "Deleted"}
