from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.infrastructure.repositories.masterflow_repository_impl import MasterFlowRepositoryImpl
from app.usecases.masterflow_usecase import MasterFlowUseCase
from app.schemas.masterflow_schema import (
    MasterFlowCreate,
    MasterFlowResponse,
    MasterFlowUpdate,
)

router = APIRouter(prefix="/api/v1/masterflow", tags=["masterflow"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_usecase(db: Session = Depends(get_db)):
    repo = MasterFlowRepositoryImpl(db)
    return MasterFlowUseCase(repo)


@router.post("/", response_model=MasterFlowResponse)
def create_masterflow(
    payload: MasterFlowCreate,
    uc: MasterFlowUseCase = Depends(get_usecase),
):
    return uc.create(
        payload.kdflow,
        payload.nmflow,
        payload.pkb,
        payload.bbn1,
        payload.bbn2,
        payload.swd,
        payload.atbkend,
        payload.flowjr,
        payload.stnkbaru,
        payload.tnkb,
        payload.sahstnk,
        payload.perpanjangstnk,
        payload.potongan,
        payload.bataslayanan,
        payload.satuan,
        payload.status,
        payload.created_by,
        payload.updated_by,
    )


@router.get("/", response_model=list[MasterFlowResponse])
def get_masterflows(uc: MasterFlowUseCase = Depends(get_usecase)):
    return uc.get_all()


@router.get("/{kdflow}", response_model=MasterFlowResponse)
def get_masterflow(kdflow: str, uc: MasterFlowUseCase = Depends(get_usecase)):
    master_flow = uc.get_by_id(kdflow)
    if not master_flow:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MasterFlow not found",
        )
    return master_flow


@router.put("/{kdflow}", response_model=MasterFlowResponse)
def update_masterflow(
    kdflow: str,
    payload: MasterFlowUpdate,
    uc: MasterFlowUseCase = Depends(get_usecase),
):
    master_flow = uc.update(
        kdflow,
        payload.nmflow,
        payload.pkb,
        payload.bbn1,
        payload.bbn2,
        payload.swd,
        payload.atbkend,
        payload.flowjr,
        payload.stnkbaru,
        payload.tnkb,
        payload.sahstnk,
        payload.perpanjangstnk,
        payload.potongan,
        payload.bataslayanan,
        payload.satuan,
        payload.status,
        payload.updated_by,
    )
    if not master_flow:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MasterFlow not found",
        )
    return master_flow


@router.delete("/{kdflow}")
def delete_masterflow(kdflow: str, uc: MasterFlowUseCase = Depends(get_usecase)):
    deleted = uc.delete(kdflow)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MasterFlow not found",
        )
    return {"message": "Deleted"}
