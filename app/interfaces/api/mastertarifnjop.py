from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.infrastructure.repositories.mastertarifnjop_repository_impl import (
    MasterTarifNjopRepositoryImpl,
)
from app.usecases.mastertarifnjop_usecase import MasterTarifNjopUseCase
from app.schemas.mastertarifnjop_schema import (
    MasterTarifNjopCreate,
    MasterTarifNjopResponse,
    MasterTarifNjopUpdate,
)

router = APIRouter(prefix="/api/v1/mastertarifnjop", tags=["MasterTarifNjop"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_usecase(db: Session = Depends(get_db)):
    repo = MasterTarifNjopRepositoryImpl(db)
    return MasterTarifNjopUseCase(repo)


@router.post("/", response_model=MasterTarifNjopResponse)
def create_mastertarifnjop(
    payload: MasterTarifNjopCreate,
    uc: MasterTarifNjopUseCase = Depends(get_usecase),
):
    return uc.create(
        payload.iduunjop,
        payload.idrekd,
        payload.kdjnstarif,
        payload.namatarif,
        payload.idmerk,
        payload.tipe,
        payload.silinder,
        payload.tahun,
        payload.kodebbm,
        payload.njop,
        payload.status,
        payload.created_by,
        payload.updated_by,
    )


@router.get("/", response_model=list[MasterTarifNjopResponse])
def get_mastertarifnjops(uc: MasterTarifNjopUseCase = Depends(get_usecase)):
    return uc.get_all()


@router.get("/{idtarifnjop}", response_model=MasterTarifNjopResponse)
def get_mastertarifnjop(
    idtarifnjop: int,
    uc: MasterTarifNjopUseCase = Depends(get_usecase),
):
    record = uc.get_by_id(idtarifnjop)
    if not record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MasterTarifNjop not found",
        )
    return record


@router.put("/{idtarifnjop}", response_model=MasterTarifNjopResponse)
def update_mastertarifnjop(
    idtarifnjop: int,
    payload: MasterTarifNjopUpdate,
    uc: MasterTarifNjopUseCase = Depends(get_usecase),
):
    record = uc.update(
        idtarifnjop,
        payload.iduunjop,
        payload.idrekd,
        payload.kdjnstarif,
        payload.namatarif,
        payload.idmerk,
        payload.tipe,
        payload.silinder,
        payload.tahun,
        payload.kodebbm,
        payload.njop,
        payload.status,
        payload.updated_by,
    )
    if not record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MasterTarifNjop not found",
        )
    return record


@router.delete("/{idtarifnjop}")
def delete_mastertarifnjop(
    idtarifnjop: int,
    uc: MasterTarifNjopUseCase = Depends(get_usecase),
):
    deleted = uc.delete(idtarifnjop)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MasterTarifNjop not found",
        )
    return {"message": "Deleted"}
