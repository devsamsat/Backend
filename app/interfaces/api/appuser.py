from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.domain.entities.appuser import AppUser
from app.infrastructure.repositories.appuser_repository_impl import AppUserRepositoryImpl
from app.usecases.appuser_usecase import AppUserUseCase
from app.schemas.appuser_schema import AppUserCreate, AppUserResponse, AppUserUpdate

router = APIRouter(prefix="/api/v1/appuser", tags=["AppUser"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_usecase(db: Session = Depends(get_db)):
    repo = AppUserRepositoryImpl(db)
    return AppUserUseCase(repo)


@router.post("/", response_model=AppUserResponse)
def create_record(payload: AppUserCreate, uc: AppUserUseCase = Depends(get_usecase)):
    entity = AppUser(
        userid=payload.userid,
        idupt=payload.idupt,
        kdtahap=payload.kdtahap,
        pwd=payload.pwd,
        idpeg=payload.idpeg,
        kdgroup=payload.kdgroup,
        nik=payload.nik,
        nama=payload.nama,
        email=payload.email,
        created_by=payload.created_by,
        updated_by=payload.updated_by,
    )
    return uc.create(entity)


@router.get("/", response_model=list[AppUserResponse])
def get_records(uc: AppUserUseCase = Depends(get_usecase)):
    return uc.get_all()


@router.get("/{userid}", response_model=AppUserResponse)
def get_record(userid: str, uc: AppUserUseCase = Depends(get_usecase)):
    record = uc.get_by_id(userid)
    if not record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Record not found",
        )
    return record


@router.put("/{userid}", response_model=AppUserResponse)
def update_record(
    userid: str,
    payload: AppUserUpdate,
    uc: AppUserUseCase = Depends(get_usecase),
):
    entity = AppUser(
        userid=userid,
        idupt=payload.idupt,
        kdtahap=payload.kdtahap,
        pwd=payload.pwd,
        idpeg=payload.idpeg,
        kdgroup=payload.kdgroup,
        nik=payload.nik,
        nama=payload.nama,
        email=payload.email,
        created_by=payload.created_by,
        updated_by=payload.updated_by,
    )
    record = uc.update(userid, entity)
    if not record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Record not found",
        )
    return record


@router.delete("/{userid}")
def delete_record(userid: str, uc: AppUserUseCase = Depends(get_usecase)):
    deleted = uc.delete(userid)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Record not found",
        )
    return {"message": "Deleted"}
