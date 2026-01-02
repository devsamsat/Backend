from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.infrastructure.repositories.masterkaupt_repository_impl import (
    MasterKauptRepositoryImpl,
)
from app.usecases.masterkaupt_usecase import MasterKauptUseCase
from app.schemas.masterkaupt_schema import (
    MasterKauptCreate,
    MasterKauptResponse,
    MasterKauptUpdate,
)

router = APIRouter(prefix="/api/v1/masterkaupt", tags=["masterkaupt"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_usecase(db: Session = Depends(get_db)):
    repo = MasterKauptRepositoryImpl(db)
    return MasterKauptUseCase(repo)


@router.post("/", response_model=MasterKauptResponse)
def create_masterkaupt(
    payload: MasterKauptCreate,
    uc: MasterKauptUseCase = Depends(get_usecase),
):
    return uc.create(
        payload.idupt,
        payload.idpegawai,
        payload.created_by,
        payload.updated_by,
    )


@router.get("/", response_model=list[MasterKauptResponse])
def get_masterkaupts(uc: MasterKauptUseCase = Depends(get_usecase)):
    return uc.get_all()


@router.get("/{idkaupt}", response_model=MasterKauptResponse)
def get_masterkaupt(
    idkaupt: int,
    uc: MasterKauptUseCase = Depends(get_usecase),
):
    master_kaupt = uc.get_by_id(idkaupt)
    if not master_kaupt:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MasterKaupt not found",
        )
    return master_kaupt


@router.put("/{idkaupt}", response_model=MasterKauptResponse)
def update_masterkaupt(
    idkaupt: int,
    payload: MasterKauptUpdate,
    uc: MasterKauptUseCase = Depends(get_usecase),
):
    master_kaupt = uc.update(
        idkaupt,
        payload.idupt,
        payload.idpegawai,
        payload.updated_by,
    )
    if not master_kaupt:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MasterKaupt not found",
        )
    return master_kaupt


@router.delete("/{idkaupt}")
def delete_masterkaupt(
    idkaupt: int,
    uc: MasterKauptUseCase = Depends(get_usecase),
):
    deleted = uc.delete(idkaupt)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MasterKaupt not found",
        )
    return {"message": "Deleted"}
