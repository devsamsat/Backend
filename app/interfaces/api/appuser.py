from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
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
def create_appuser(payload: AppUserCreate, uc: AppUserUseCase = Depends(get_usecase)):
    return uc.create(
        payload.userid,
        payload.kdtahap,
        payload.kdgroup,
        payload.idupt,
        payload.pwd,
        payload.idpeg,
        payload.nik,
        payload.nama,
        payload.email,
        payload.created_by,
        payload.updated_by,
    )


@router.get("/", response_model=list[AppUserResponse])
def get_appusers(uc: AppUserUseCase = Depends(get_usecase)):
    return uc.get_all()


@router.get("/{userid}", response_model=AppUserResponse)
def get_appuser(userid: str, uc: AppUserUseCase = Depends(get_usecase)):
    app_user = uc.get_by_id(userid)
    if not app_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="AppUser not found")
    return app_user


@router.put("/{userid}", response_model=AppUserResponse)
def update_appuser(
    userid: str,
    payload: AppUserUpdate,
    uc: AppUserUseCase = Depends(get_usecase),
):
    app_user = uc.update(
        userid,
        payload.kdtahap,
        payload.kdgroup,
        payload.idupt,
        payload.pwd,
        payload.idpeg,
        payload.nik,
        payload.nama,
        payload.email,
        payload.updated_by,
    )
    if not app_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="AppUser not found")
    return app_user


@router.delete("/{userid}")
def delete_appuser(userid: str, uc: AppUserUseCase = Depends(get_usecase)):
    deleted = uc.delete(userid)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="AppUser not found")
    return {"message": "Deleted"}
