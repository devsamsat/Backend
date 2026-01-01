from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.infrastructure.repositories.transhistpendataandet_repository_impl import (
    TransHistPendataanDetRepositoryImpl,
)
from app.usecases.transhistpendataandet_usecase import TransHistPendataanDetUseCase
from app.schemas.transhistpendataandet_schema import (
    TransHistPendataanDetCreate,
    TransHistPendataanDetResponse,
    TransHistPendataanDetUpdate,
)

router = APIRouter(prefix="/api/v1/transhistpendataandet", tags=["TransHistPendataanDet"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_usecase(db: Session = Depends(get_db)):
    repo = TransHistPendataanDetRepositoryImpl(db)
    return TransHistPendataanDetUseCase(repo)


@router.post("/", response_model=TransHistPendataanDetResponse)
def create_transhistpendataandet(
    payload: TransHistPendataanDetCreate,
    uc: TransHistPendataanDetUseCase = Depends(get_usecase),
):
    return uc.create(
        payload.idhistpendataan,
        payload.idpenetapan,
        payload.nourut,
        payload.transid,
        payload.ket1,
        payload.usahaid,
        payload.tarifpajak,
        payload.histid,
        payload.status,
        payload.lokasi,
        payload.created_by,
        payload.updated_by,
    )


@router.get("/", response_model=list[TransHistPendataanDetResponse])
def get_transhistpendataandets(uc: TransHistPendataanDetUseCase = Depends(get_usecase)):
    return uc.get_all()


@router.get("/{idhistpendataandet}", response_model=TransHistPendataanDetResponse)
def get_transhistpendataandet(
    idhistpendataandet: int,
    uc: TransHistPendataanDetUseCase = Depends(get_usecase),
):
    record = uc.get_by_id(idhistpendataandet)
    if not record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="TransHistPendataanDet not found",
        )
    return record


@router.put("/{idhistpendataandet}", response_model=TransHistPendataanDetResponse)
def update_transhistpendataandet(
    idhistpendataandet: int,
    payload: TransHistPendataanDetUpdate,
    uc: TransHistPendataanDetUseCase = Depends(get_usecase),
):
    record = uc.update(
        idhistpendataandet,
        payload.idhistpendataan,
        payload.idpenetapan,
        payload.nourut,
        payload.transid,
        payload.ket1,
        payload.usahaid,
        payload.tarifpajak,
        payload.histid,
        payload.status,
        payload.lokasi,
        payload.updated_by,
    )
    if not record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="TransHistPendataanDet not found",
        )
    return record


@router.delete("/{idhistpendataandet}")
def delete_transhistpendataandet(
    idhistpendataandet: int,
    uc: TransHistPendataanDetUseCase = Depends(get_usecase),
):
    deleted = uc.delete(idhistpendataandet)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="TransHistPendataanDet not found",
        )
    return {"message": "Deleted"}
