from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.infrastructure.repositories.masterkbdet_repository_impl import (
    MasterKbDetRepositoryImpl,
)
from app.usecases.masterkbdet_usecase import MasterKbDetUseCase
from app.schemas.masterkbdet_schema import (
    MasterKbDetCreate,
    MasterKbDetResponse,
    MasterKbDetUpdate,
)

router = APIRouter(prefix="/api/v1/masterkbdet", tags=["masterkbdet"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_usecase(db: Session = Depends(get_db)):
    repo = MasterKbDetRepositoryImpl(db)
    return MasterKbDetUseCase(repo)


@router.post("/", response_model=MasterKbDetResponse)
def create_masterkbdet(
    payload: MasterKbDetCreate,
    uc: MasterKbDetUseCase = Depends(get_usecase),
):
    return uc.create(
        payload.idkb,
        payload.idjnsd,
        payload.created_by,
        payload.updated_by,
    )


@router.get("/", response_model=list[MasterKbDetResponse])
def get_masterkbdets(uc: MasterKbDetUseCase = Depends(get_usecase)):
    return uc.get_all()


@router.get("/{idkbdet}", response_model=MasterKbDetResponse)
def get_masterkbdet(
    idkbdet: int,
    uc: MasterKbDetUseCase = Depends(get_usecase),
):
    master_kbdet = uc.get_by_id(idkbdet)
    if not master_kbdet:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MasterKbDet not found",
        )
    return master_kbdet


@router.put("/{idkbdet}", response_model=MasterKbDetResponse)
def update_masterkbdet(
    idkbdet: int,
    payload: MasterKbDetUpdate,
    uc: MasterKbDetUseCase = Depends(get_usecase),
):
    master_kbdet = uc.update(
        idkbdet,
        payload.idkb,
        payload.idjnsd,
        payload.updated_by,
    )
    if not master_kbdet:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MasterKbDet not found",
        )
    return master_kbdet


@router.delete("/{idkbdet}")
def delete_masterkbdet(
    idkbdet: int,
    uc: MasterKbDetUseCase = Depends(get_usecase),
):
    deleted = uc.delete(idkbdet)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MasterKbDet not found",
        )
    return {"message": "Deleted"}
