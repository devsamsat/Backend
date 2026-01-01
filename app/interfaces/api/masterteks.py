from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.infrastructure.repositories.masterteks_repository_impl import MasterTeksRepositoryImpl
from app.usecases.masterteks_usecase import MasterTeksUseCase
from app.schemas.masterteks_schema import MasterTeksCreate, MasterTeksResponse, MasterTeksUpdate

router = APIRouter(prefix="/api/v1/masterteks", tags=["MasterTeks"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_usecase(db: Session = Depends(get_db)):
    repo = MasterTeksRepositoryImpl(db)
    return MasterTeksUseCase(repo)


@router.post("/", response_model=MasterTeksResponse)
def create_masterteks(
    payload: MasterTeksCreate,
    uc: MasterTeksUseCase = Depends(get_usecase),
):
    return uc.create(
        payload.datateks,
        payload.status,
        payload.created_by,
        payload.updated_by,
    )


@router.get("/", response_model=list[MasterTeksResponse])
def get_masterteks(uc: MasterTeksUseCase = Depends(get_usecase)):
    return uc.get_all()


@router.get("/{idteks}", response_model=MasterTeksResponse)
def get_masterteks_by_id(
    idteks: int,
    uc: MasterTeksUseCase = Depends(get_usecase),
):
    record = uc.get_by_id(idteks)
    if not record:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="MasterTeks not found")
    return record


@router.put("/{idteks}", response_model=MasterTeksResponse)
def update_masterteks(
    idteks: int,
    payload: MasterTeksUpdate,
    uc: MasterTeksUseCase = Depends(get_usecase),
):
    record = uc.update(
        idteks,
        payload.datateks,
        payload.status,
        payload.updated_by,
    )
    if not record:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="MasterTeks not found")
    return record


@router.delete("/{idteks}")
def delete_masterteks(
    idteks: int,
    uc: MasterTeksUseCase = Depends(get_usecase),
):
    deleted = uc.delete(idteks)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="MasterTeks not found")
    return {"message": "Deleted"}
