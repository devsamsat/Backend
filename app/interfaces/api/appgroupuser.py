from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.domain.entities.appgroupuser import AppGroupUser
from app.infrastructure.repositories.appgroupuser_repository_impl import (
    AppGroupUserRepositoryImpl,
)
from app.usecases.appgroupuser_usecase import AppGroupUserUseCase
from app.schemas.appgroupuser_schema import (
    AppGroupUserCreate,
    AppGroupUserResponse,
    AppGroupUserUpdate,
)

router = APIRouter(prefix="/api/v1/appgroupuser", tags=["AppGroupUser"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_usecase(db: Session = Depends(get_db)):
    repo = AppGroupUserRepositoryImpl(db)
    return AppGroupUserUseCase(repo)


@router.post("/", response_model=AppGroupUserResponse)
def create_record(
    payload: AppGroupUserCreate,
    uc: AppGroupUserUseCase = Depends(get_usecase),
):
    entity = AppGroupUser(
        kdgroup=payload.kdgroup,
        nmgroup=payload.nmgroup,
        ket=payload.ket,
        created_by=payload.created_by,
        updated_by=payload.updated_by,
    )
    return uc.create(entity)


@router.get("/", response_model=list[AppGroupUserResponse])
def get_records(uc: AppGroupUserUseCase = Depends(get_usecase)):
    return uc.get_all()


@router.get("/{kdgroup}", response_model=AppGroupUserResponse)
def get_record(kdgroup: str, uc: AppGroupUserUseCase = Depends(get_usecase)):
    record = uc.get_by_id(kdgroup)
    if not record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Record not found",
        )
    return record


@router.put("/{kdgroup}", response_model=AppGroupUserResponse)
def update_record(
    kdgroup: str,
    payload: AppGroupUserUpdate,
    uc: AppGroupUserUseCase = Depends(get_usecase),
):
    entity = AppGroupUser(
        kdgroup=kdgroup,
        nmgroup=payload.nmgroup,
        ket=payload.ket,
        created_by=payload.created_by,
        updated_by=payload.updated_by,
    )
    record = uc.update(kdgroup, entity)
    if not record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Record not found",
        )
    return record


@router.delete("/{kdgroup}")
def delete_record(kdgroup: str, uc: AppGroupUserUseCase = Depends(get_usecase)):
    deleted = uc.delete(kdgroup)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Record not found",
        )
    return {"message": "Deleted"}
