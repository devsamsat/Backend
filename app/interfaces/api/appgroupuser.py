from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
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
def create_appgroupuser(
    payload: AppGroupUserCreate,
    uc: AppGroupUserUseCase = Depends(get_usecase),
):
    return uc.create(
        payload.kdgroup,
        payload.nmgroup,
        payload.ket,
        payload.created_by,
        payload.updated_by,
    )


@router.get("/", response_model=list[AppGroupUserResponse])
def get_appgroupusers(uc: AppGroupUserUseCase = Depends(get_usecase)):
    return uc.get_all()


@router.get("/{kdgroup}", response_model=AppGroupUserResponse)
def get_appgroupuser(
    kdgroup: str,
    uc: AppGroupUserUseCase = Depends(get_usecase),
):
    group_user = uc.get_by_id(kdgroup)
    if not group_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="AppGroupUser not found",
        )
    return group_user


@router.put("/{kdgroup}", response_model=AppGroupUserResponse)
def update_appgroupuser(
    kdgroup: str,
    payload: AppGroupUserUpdate,
    uc: AppGroupUserUseCase = Depends(get_usecase),
):
    group_user = uc.update(
        kdgroup,
        payload.nmgroup,
        payload.ket,
        payload.updated_by,
    )
    if not group_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="AppGroupUser not found",
        )
    return group_user


@router.delete("/{kdgroup}")
def delete_appgroupuser(
    kdgroup: str,
    uc: AppGroupUserUseCase = Depends(get_usecase),
):
    deleted = uc.delete(kdgroup)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="AppGroupUser not found",
        )
    return {"message": "Deleted"}
