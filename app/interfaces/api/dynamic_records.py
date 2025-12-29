from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.infrastructure.repositories.dynamic_record_repository_impl import (
    DynamicRecordRepositoryImpl,
)
from app.usecases.dynamic_record_usecase import DynamicRecordUseCase
from app.schemas.dynamic_schema import (
    DynamicRecordCreate,
    DynamicRecordResponse,
    DynamicRecordUpdate,
)

router = APIRouter(prefix="/api/v1/dynamic_records", tags=["Dynamic Records"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_usecase(db: Session = Depends(get_db)):
    repo = DynamicRecordRepositoryImpl(db)
    return DynamicRecordUseCase(repo)


@router.post("/", response_model=DynamicRecordResponse)
def create_record(
    payload: DynamicRecordCreate,
    uc: DynamicRecordUseCase = Depends(get_usecase),
):
    return uc.create(payload.table_name, payload.record_id, payload.payload)


@router.get("/", response_model=list[DynamicRecordResponse])
def get_records(uc: DynamicRecordUseCase = Depends(get_usecase)):
    return uc.get_all()


@router.get("/{record_id}", response_model=DynamicRecordResponse)
def get_record(
    record_id: int,
    uc: DynamicRecordUseCase = Depends(get_usecase),
):
    record = uc.get_by_id(record_id)
    if not record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Record not found",
        )
    return record


@router.put("/{record_id}", response_model=DynamicRecordResponse)
def update_record(
    record_id: int,
    payload: DynamicRecordUpdate,
    uc: DynamicRecordUseCase = Depends(get_usecase),
):
    record = uc.update(
        record_id,
        payload.table_name,
        payload.record_id,
        payload.payload,
    )
    if not record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Record not found",
        )
    return record


@router.delete("/{record_id}")
def delete_record(
    record_id: int,
    uc: DynamicRecordUseCase = Depends(get_usecase),
):
    deleted = uc.delete(record_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Record not found",
        )
    return {"message": "Deleted"}
