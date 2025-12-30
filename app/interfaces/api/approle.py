from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.domain.entities.approle import AppRole
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
def create_record(payload: AppRoleCreate, uc: AppRoleUseCase = Depends(get_usecase)):
    entity = AppRole(
        roleid=payload.roleid,
        idapp=payload.idapp,
        role=payload.role,
        role_type=payload.role_type,
        menuid=payload.menuid,
        parentid=payload.parentid,
        bantuan=payload.bantuan,
        link=payload.link,
        icon=payload.icon,
        kdlevel=payload.kdlevel,
        is_show=payload.is_show,
        created_by=payload.created_by,
        updated_by=payload.updated_by,
    )
    return uc.create(entity)


@router.get("/", response_model=list[AppRoleResponse])
def get_records(uc: AppRoleUseCase = Depends(get_usecase)):
    return uc.get_all()


@router.get("/{roleid}", response_model=AppRoleResponse)
def get_record(roleid: str, uc: AppRoleUseCase = Depends(get_usecase)):
    record = uc.get_by_id(roleid)
    if not record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Record not found",
        )
    return record


@router.put("/{roleid}", response_model=AppRoleResponse)
def update_record(
    roleid: str,
    payload: AppRoleUpdate,
    uc: AppRoleUseCase = Depends(get_usecase),
):
    entity = AppRole(
        roleid=roleid,
        idapp=payload.idapp,
        role=payload.role,
        role_type=payload.role_type,
        menuid=payload.menuid,
        parentid=payload.parentid,
        bantuan=payload.bantuan,
        link=payload.link,
        icon=payload.icon,
        kdlevel=payload.kdlevel,
        is_show=payload.is_show,
        created_by=payload.created_by,
        updated_by=payload.updated_by,
    )
    record = uc.update(roleid, entity)
    if not record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Record not found",
        )
    return record


@router.delete("/{roleid}")
def delete_record(roleid: str, uc: AppRoleUseCase = Depends(get_usecase)):
    deleted = uc.delete(roleid)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Record not found",
        )
    return {"message": "Deleted"}
