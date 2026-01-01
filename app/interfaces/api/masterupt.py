from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.infrastructure.repositories.masterupt_repository_impl import MasterUptRepositoryImpl
from app.usecases.masterupt_usecase import MasterUptUseCase
from app.schemas.masterupt_schema import MasterUptCreate, MasterUptResponse, MasterUptUpdate

router = APIRouter(prefix="/api/v1/masterupt", tags=["MasterUpt"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_usecase(db: Session = Depends(get_db)):
    repo = MasterUptRepositoryImpl(db)
    return MasterUptUseCase(repo)


@router.post("/", response_model=MasterUptResponse)
def create_masterupt(
    payload: MasterUptCreate,
    uc: MasterUptUseCase = Depends(get_usecase),
):
    return uc.create(
        payload.kdupt,
        payload.nmupt,
        payload.upt_type,
        payload.idparent,
        payload.kdlevel,
        payload.akroupt,
        payload.alamat,
        payload.telepon,
        payload.idbank,
        payload.idkabkota,
        payload.kepala,
        payload.koordinator,
        payload.bendahara,
        payload.norekb,
        payload.status,
        payload.created_by,
        payload.updated_by,
    )


@router.get("/", response_model=list[MasterUptResponse])
def get_masterupts(uc: MasterUptUseCase = Depends(get_usecase)):
    return uc.get_all()


@router.get("/{idupt}", response_model=MasterUptResponse)
def get_masterupt(
    idupt: int,
    uc: MasterUptUseCase = Depends(get_usecase),
):
    record = uc.get_by_id(idupt)
    if not record:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="MasterUpt not found")
    return record


@router.put("/{idupt}", response_model=MasterUptResponse)
def update_masterupt(
    idupt: int,
    payload: MasterUptUpdate,
    uc: MasterUptUseCase = Depends(get_usecase),
):
    record = uc.update(
        idupt,
        payload.kdupt,
        payload.nmupt,
        payload.upt_type,
        payload.idparent,
        payload.kdlevel,
        payload.akroupt,
        payload.alamat,
        payload.telepon,
        payload.idbank,
        payload.idkabkota,
        payload.kepala,
        payload.koordinator,
        payload.bendahara,
        payload.norekb,
        payload.status,
        payload.updated_by,
    )
    if not record:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="MasterUpt not found")
    return record


@router.delete("/{idupt}")
def delete_masterupt(
    idupt: int,
    uc: MasterUptUseCase = Depends(get_usecase),
):
    deleted = uc.delete(idupt)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="MasterUpt not found")
    return {"message": "Deleted"}
