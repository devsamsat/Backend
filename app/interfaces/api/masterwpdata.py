from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.infrastructure.repositories.masterwpdata_repository_impl import (
    MasterWpDataRepositoryImpl,
)
from app.usecases.masterwpdata_usecase import MasterWpDataUseCase
from app.schemas.masterwpdata_schema import (
    MasterWpDataCreate,
    MasterWpDataResponse,
    MasterWpDataUpdate,
)

router = APIRouter(prefix="/api/v1/masterwpdata", tags=["MasterWpData"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_usecase(db: Session = Depends(get_db)):
    repo = MasterWpDataRepositoryImpl(db)
    return MasterWpDataUseCase(repo)


@router.post("/", response_model=MasterWpDataResponse)
def create_masterwpdata(
    payload: MasterWpDataCreate,
    uc: MasterWpDataUseCase = Depends(get_usecase),
):
    return uc.create(
        payload.idjnsd,
        payload.idwp,
        payload.tglpendataan,
        payload.created_by,
        payload.updated_by,
    )


@router.get("/", response_model=list[MasterWpDataResponse])
def get_masterwpdatas(uc: MasterWpDataUseCase = Depends(get_usecase)):
    return uc.get_all()


@router.get("/{idwpdata}", response_model=MasterWpDataResponse)
def get_masterwpdata(
    idwpdata: int,
    uc: MasterWpDataUseCase = Depends(get_usecase),
):
    record = uc.get_by_id(idwpdata)
    if not record:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="MasterWpData not found")
    return record


@router.put("/{idwpdata}", response_model=MasterWpDataResponse)
def update_masterwpdata(
    idwpdata: int,
    payload: MasterWpDataUpdate,
    uc: MasterWpDataUseCase = Depends(get_usecase),
):
    record = uc.update(
        idwpdata,
        payload.idjnsd,
        payload.idwp,
        payload.tglpendataan,
        payload.updated_by,
    )
    if not record:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="MasterWpData not found")
    return record


@router.delete("/{idwpdata}")
def delete_masterwpdata(
    idwpdata: int,
    uc: MasterWpDataUseCase = Depends(get_usecase),
):
    deleted = uc.delete(idwpdata)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="MasterWpData not found")
    return {"message": "Deleted"}
