from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.infrastructure.repositories.appotor_repository_impl import AppOtorRepositoryImpl
from app.usecases.appotor_usecase import AppOtorUseCase
from app.schemas.appotor_schema import AppOtorCreate, AppOtorResponse, AppOtorUpdate

router = APIRouter(prefix="/api/v1/appotor", tags=["AppOtor"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_usecase(db: Session = Depends(get_db)):
    repo = AppOtorRepositoryImpl(db)
    return AppOtorUseCase(repo)


@router.post("/", response_model=AppOtorResponse)
def create_appotor(payload: AppOtorCreate, uc: AppOtorUseCase = Depends(get_usecase)):
    return uc.create(
        payload.kdgroup,
        payload.roleid,
        payload.ket,
        payload.created_by,
        payload.updated_by,
    )


@router.get("/", response_model=list[AppOtorResponse])
def get_appotors(uc: AppOtorUseCase = Depends(get_usecase)):
    return uc.get_all()


@router.get("/{kdgroup}/{roleid}", response_model=AppOtorResponse)
def get_appotor(
    kdgroup: str,
    roleid: str,
    uc: AppOtorUseCase = Depends(get_usecase),
):
    app_otor = uc.get_by_id(kdgroup, roleid)
    if not app_otor:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="AppOtor not found",
        )
    return app_otor


@router.put("/{kdgroup}/{roleid}", response_model=AppOtorResponse)
def update_appotor(
    kdgroup: str,
    roleid: str,
    payload: AppOtorUpdate,
    uc: AppOtorUseCase = Depends(get_usecase),
):
    app_otor = uc.update(
        kdgroup,
        roleid,
        payload.ket,
        payload.updated_by,
    )
    if not app_otor:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="AppOtor not found",
        )
    return app_otor


@router.delete("/{kdgroup}/{roleid}")
def delete_appotor(
    kdgroup: str,
    roleid: str,
    uc: AppOtorUseCase = Depends(get_usecase),
):
    deleted = uc.delete(kdgroup, roleid)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="AppOtor not found",
        )
    return {"message": "Deleted"}
