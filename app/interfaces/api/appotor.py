from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.domain.entities.appotor import AppOtor
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
def create_record(payload: AppOtorCreate, uc: AppOtorUseCase = Depends(get_usecase)):
    entity = AppOtor(
        kdgroup=payload.kdgroup,
        roleid=payload.roleid,
        ket=payload.ket,
        created_by=payload.created_by,
        updated_by=payload.updated_by,
    )
    return uc.create(entity)


@router.get("/", response_model=list[AppOtorResponse])
def get_records(uc: AppOtorUseCase = Depends(get_usecase)):
    return uc.get_all()


@router.get("/{kdgroup}/{roleid}", response_model=AppOtorResponse)
def get_record(
    kdgroup: str,
    roleid: str,
    uc: AppOtorUseCase = Depends(get_usecase),
):
    record = uc.get_by_id(kdgroup, roleid)
    if not record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Record not found",
        )
    return record


@router.put("/{kdgroup}/{roleid}", response_model=AppOtorResponse)
def update_record(
    kdgroup: str,
    roleid: str,
    payload: AppOtorUpdate,
    uc: AppOtorUseCase = Depends(get_usecase),
):
    entity = AppOtor(
        kdgroup=kdgroup,
        roleid=roleid,
        ket=payload.ket,
        created_by=payload.created_by,
        updated_by=payload.updated_by,
    )
    record = uc.update(kdgroup, roleid, entity)
    if not record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Record not found",
        )
    return record


@router.delete("/{kdgroup}/{roleid}")
def delete_record(
    kdgroup: str,
    roleid: str,
    uc: AppOtorUseCase = Depends(get_usecase),
):
    deleted = uc.delete(kdgroup, roleid)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Record not found",
        )
    return {"message": "Deleted"}
