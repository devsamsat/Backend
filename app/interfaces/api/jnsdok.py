from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.domain.entities.jnsdok import JnsDok
from app.infrastructure.repositories.jnsdok_repository_impl import JnsDokRepositoryImpl
from app.usecases.jnsdok_usecase import JnsDokUseCase
from app.schemas.jnsdok_schema import JnsDokCreate, JnsDokResponse, JnsDokUpdate

router = APIRouter(prefix="/api/v1/jnsdok", tags=["JnsDok"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_usecase(db: Session = Depends(get_db)):
    repo = JnsDokRepositoryImpl(db)
    return JnsDokUseCase(repo)


@router.post("/", response_model=JnsDokResponse)
def create_record(payload: JnsDokCreate, uc: JnsDokUseCase = Depends(get_usecase)):
    entity = JnsDok(
        kddok=payload.kddok,
        namadok=payload.namadok,
        keterangan=payload.keterangan,
        created_by=payload.created_by,
        updated_by=payload.updated_by,
    )
    return uc.create(entity)


@router.get("/", response_model=list[JnsDokResponse])
def get_records(uc: JnsDokUseCase = Depends(get_usecase)):
    return uc.get_all()


@router.get("/{kddok}", response_model=JnsDokResponse)
def get_record(kddok: str, uc: JnsDokUseCase = Depends(get_usecase)):
    record = uc.get_by_id(kddok)
    if not record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Record not found",
        )
    return record


@router.put("/{kddok}", response_model=JnsDokResponse)
def update_record(
    kddok: str,
    payload: JnsDokUpdate,
    uc: JnsDokUseCase = Depends(get_usecase),
):
    entity = JnsDok(
        kddok=kddok,
        namadok=payload.namadok,
        keterangan=payload.keterangan,
        created_by=payload.created_by,
        updated_by=payload.updated_by,
    )
    record = uc.update(kddok, entity)
    if not record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Record not found",
        )
    return record


@router.delete("/{kddok}")
def delete_record(kddok: str, uc: JnsDokUseCase = Depends(get_usecase)):
    deleted = uc.delete(kddok)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Record not found",
        )
    return {"message": "Deleted"}
