from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.domain.entities.jnshist import JnsHist
from app.infrastructure.repositories.jnshist_repository_impl import JnsHistRepositoryImpl
from app.usecases.jnshist_usecase import JnsHistUseCase
from app.schemas.jnshist_schema import JnsHistCreate, JnsHistResponse, JnsHistUpdate

router = APIRouter(prefix="/api/v1/jnshist", tags=["JnsHist"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_usecase(db: Session = Depends(get_db)):
    repo = JnsHistRepositoryImpl(db)
    return JnsHistUseCase(repo)


@router.post("/", response_model=JnsHistResponse)
def create_record(payload: JnsHistCreate, uc: JnsHistUseCase = Depends(get_usecase)):
    entity = JnsHist(
        kdhist=payload.kdhist,
        nmhist=payload.nmhist,
        kdflow=payload.kdflow,
        status=payload.status,
        created_by=payload.created_by,
        updated_by=payload.updated_by,
    )
    return uc.create(entity)


@router.get("/", response_model=list[JnsHistResponse])
def get_records(uc: JnsHistUseCase = Depends(get_usecase)):
    return uc.get_all()


@router.get("/{kdhist}", response_model=JnsHistResponse)
def get_record(kdhist: str, uc: JnsHistUseCase = Depends(get_usecase)):
    record = uc.get_by_id(kdhist)
    if not record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Record not found",
        )
    return record


@router.put("/{kdhist}", response_model=JnsHistResponse)
def update_record(
    kdhist: str,
    payload: JnsHistUpdate,
    uc: JnsHistUseCase = Depends(get_usecase),
):
    entity = JnsHist(
        kdhist=kdhist,
        nmhist=payload.nmhist,
        kdflow=payload.kdflow,
        status=payload.status,
        created_by=payload.created_by,
        updated_by=payload.updated_by,
    )
    record = uc.update(kdhist, entity)
    if not record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Record not found",
        )
    return record


@router.delete("/{kdhist}")
def delete_record(kdhist: str, uc: JnsHistUseCase = Depends(get_usecase)):
    deleted = uc.delete(kdhist)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Record not found",
        )
    return {"message": "Deleted"}
