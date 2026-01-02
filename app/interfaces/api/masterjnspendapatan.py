from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.infrastructure.repositories.masterjnspendapatan_repository_impl import (
    MasterJnsPendapatanRepositoryImpl,
)
from app.usecases.masterjnspendapatan_usecase import MasterJnsPendapatanUseCase
from app.schemas.masterjnspendapatan_schema import (
    MasterJnsPendapatanCreate,
    MasterJnsPendapatanResponse,
    MasterJnsPendapatanUpdate,
)

router = APIRouter(prefix="/api/v1/masterjnspendapatan", tags=["masterjnspendapatan"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_usecase(db: Session = Depends(get_db)):
    repo = MasterJnsPendapatanRepositoryImpl(db)
    return MasterJnsPendapatanUseCase(repo)


@router.post("/", response_model=MasterJnsPendapatanResponse)
def create_masterjnspendapatan(
    payload: MasterJnsPendapatanCreate,
    uc: MasterJnsPendapatanUseCase = Depends(get_usecase),
):
    return uc.create(
        payload.nmjnspendapatan,
        payload.parentid,
        payload.kdrek,
        payload.jatuhtempo,
        payload.status,
        payload.selfassessment,
        payload.katid,
        payload.created_by,
        payload.updated_by,
    )


@router.get("/", response_model=list[MasterJnsPendapatanResponse])
def get_masterjnspendapatans(uc: MasterJnsPendapatanUseCase = Depends(get_usecase)):
    return uc.get_all()


@router.get("/{idjnsd}", response_model=MasterJnsPendapatanResponse)
def get_masterjnspendapatan(
    idjnsd: int,
    uc: MasterJnsPendapatanUseCase = Depends(get_usecase),
):
    master_jns_pendapatan = uc.get_by_id(idjnsd)
    if not master_jns_pendapatan:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MasterJnsPendapatan not found",
        )
    return master_jns_pendapatan


@router.put("/{idjnsd}", response_model=MasterJnsPendapatanResponse)
def update_masterjnspendapatan(
    idjnsd: int,
    payload: MasterJnsPendapatanUpdate,
    uc: MasterJnsPendapatanUseCase = Depends(get_usecase),
):
    master_jns_pendapatan = uc.update(
        idjnsd,
        payload.nmjnspendapatan,
        payload.parentid,
        payload.kdrek,
        payload.jatuhtempo,
        payload.status,
        payload.selfassessment,
        payload.katid,
        payload.updated_by,
    )
    if not master_jns_pendapatan:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MasterJnsPendapatan not found",
        )
    return master_jns_pendapatan


@router.delete("/{idjnsd}")
def delete_masterjnspendapatan(
    idjnsd: int,
    uc: MasterJnsPendapatanUseCase = Depends(get_usecase),
):
    deleted = uc.delete(idjnsd)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MasterJnsPendapatan not found",
        )
    return {"message": "Deleted"}
