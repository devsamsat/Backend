from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.domain.entities.jnsjr import JnsJr
from app.infrastructure.repositories.jnsjr_repository_impl import JnsJrRepositoryImpl
from app.usecases.jnsjr_usecase import JnsJrUseCase
from app.schemas.jnsjr_schema import JnsJrCreate, JnsJrResponse, JnsJrUpdate

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
def create_record(payload: JnsJrCreate, uc: JnsJrUseCase = Depends(get_usecase)):
    entity = JnsJr(
        jnsjrid=payload.jnsjrid,
        kodejr=payload.kodejr,
        goljns=payload.goljns,
        pu=payload.pu,
        roda=payload.roda,
        keterangan=payload.keterangan,
        created_by=payload.created_by,
        updated_by=payload.updated_by,
    )
    return uc.create(entity)


@router.get("/", response_model=list[JnsJrResponse])
def get_records(uc: JnsJrUseCase = Depends(get_usecase)):
    return uc.get_all()


@router.get("/{jnsjrid}", response_model=JnsJrResponse)
def get_record(jnsjrid: str, uc: JnsJrUseCase = Depends(get_usecase)):
    record = uc.get_by_id(jnsjrid)
    if not record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Record not found",
        )
    return record


@router.put("/{jnsjrid}", response_model=JnsJrResponse)
def update_record(
    jnsjrid: str,
    payload: JnsJrUpdate,
    uc: JnsJrUseCase = Depends(get_usecase),
):
    entity = JnsJr(
        jnsjrid=jnsjrid,
        kodejr=payload.kodejr,
        goljns=payload.goljns,
        pu=payload.pu,
        roda=payload.roda,
        keterangan=payload.keterangan,
        created_by=payload.created_by,
        updated_by=payload.updated_by,
    )
    record = uc.update(jnsjrid, entity)
    if not record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Record not found",
        )
    return record


@router.delete("/{jnsjrid}")
def delete_record(jnsjrid: str, uc: JnsJrUseCase = Depends(get_usecase)):
    deleted = uc.delete(jnsjrid)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Record not found",
        )
    return {"message": "Deleted"}
