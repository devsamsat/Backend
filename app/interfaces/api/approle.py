from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.infrastructure.repositories.approle_repository_impl import AppRoleRepositoryImpl
from app.usecases.approle_usecase import AppRoleUseCase
from app.schemas.approle_schema import AppRoleCreate, AppRoleResponse, AppRoleUpdate

router = APIRouter(prefix="/api/v1/approle", tags=["AppRole"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_usecase(db: Session = Depends(get_db)):
    repo = AppRoleRepositoryImpl(db)
    return AppRoleUseCase(repo)


@router.post("/", response_model=AppRoleResponse)
def create_approle(payload: AppRoleCreate, uc: AppRoleUseCase = Depends(get_usecase)):
    return uc.create(
        payload.roleid,
        payload.idapp,
        payload.role,
        payload.role_type,
        payload.menuid,
        payload.parentid,
        payload.bantuan,
        payload.link,
        payload.icon,
        payload.kdlevel,
        payload.is_show,
        payload.created_by,
        payload.updated_by,
    )


@router.get("/", response_model=list[AppRoleResponse])
def get_approles(uc: AppRoleUseCase = Depends(get_usecase)):
    return uc.get_all()


@router.get("/{roleid}", response_model=AppRoleResponse)
def get_approle(roleid: str, uc: AppRoleUseCase = Depends(get_usecase)):
    app_role = uc.get_by_id(roleid)
    if not app_role:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="AppRole not found")
    return app_role


@router.put("/{roleid}", response_model=AppRoleResponse)
def update_approle(
    roleid: str,
    payload: AppRoleUpdate,
    uc: AppRoleUseCase = Depends(get_usecase),
):
    app_role = uc.update(
        roleid,
        payload.idapp,
        payload.role,
        payload.role_type,
        payload.menuid,
        payload.parentid,
        payload.bantuan,
        payload.link,
        payload.icon,
        payload.kdlevel,
        payload.is_show,
        payload.updated_by,
    )
    if not app_role:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="AppRole not found")
    return app_role


@router.delete("/{roleid}")
def delete_approle(roleid: str, uc: AppRoleUseCase = Depends(get_usecase)):
    deleted = uc.delete(roleid)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="AppRole not found")
    return {"message": "Deleted"}
