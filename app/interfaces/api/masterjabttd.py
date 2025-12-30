from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.infrastructure.repositories.masterjabttd_repository_impl import (
    MasterJabTtdRepositoryImpl,
)
from app.usecases.masterjabttd_usecase import MasterJabTtdUseCase
from app.schemas.masterjabttd_schema import (
    MasterJabTtdCreate,
    MasterJabTtdResponse,
    MasterJabTtdUpdate,
)

router = APIRouter(prefix="/api/v1/masterjabttd", tags=["masterjabttd"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_usecase(db: Session = Depends(get_db)):
    repo = MasterJabTtdRepositoryImpl(db)
    return MasterJabTtdUseCase(repo)


@router.post("/", response_model=MasterJabTtdResponse)
def create_masterjabttd(
    payload: MasterJabTtdCreate,
    uc: MasterJabTtdUseCase = Depends(get_usecase),
):
    return uc.create(
        payload.idpegawai,
        payload.kddok,
        payload.jabatan,
        payload.ket,
        payload.status,
        payload.created_by,
        payload.updated_by,
    )


@router.get("/", response_model=list[MasterJabTtdResponse])
def get_masterjabttds(uc: MasterJabTtdUseCase = Depends(get_usecase)):
    return uc.get_all()


@router.get("/{idjabttd}", response_model=MasterJabTtdResponse)
def get_masterjabttd(idjabttd: int, uc: MasterJabTtdUseCase = Depends(get_usecase)):
    master_jab_ttd = uc.get_by_id(idjabttd)
    if not master_jab_ttd:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MasterJabTtd not found",
        )
    return master_jab_ttd


@router.put("/{idjabttd}", response_model=MasterJabTtdResponse)
def update_masterjabttd(
    idjabttd: int,
    payload: MasterJabTtdUpdate,
    uc: MasterJabTtdUseCase = Depends(get_usecase),
):
    master_jab_ttd = uc.update(
        idjabttd,
        payload.idpegawai,
        payload.kddok,
        payload.jabatan,
        payload.ket,
        payload.status,
        payload.updated_by,
    )
    if not master_jab_ttd:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MasterJabTtd not found",
        )
    return master_jab_ttd


@router.delete("/{idjabttd}")
def delete_masterjabttd(idjabttd: int, uc: MasterJabTtdUseCase = Depends(get_usecase)):
    deleted = uc.delete(idjabttd)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MasterJabTtd not found",
        )
    return {"message": "Deleted"}
