from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.infrastructure.repositories.jnsdok_repository_impl import JnsDokRepositoryImpl
from app.usecases.jnsdok_usecase import JnsDokUseCase
from app.schemas.jnsdok_schema import JnsDokCreate, JnsDokResponse, JnsDokUpdate

router = APIRouter(prefix="/api/v1/jnsdok", tags=["JnsDok"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_usecase(db: Session = Depends(get_db)):
    repo = JnsDokRepositoryImpl(db)
    return JnsDokUseCase(repo)


@router.post("/", response_model=JnsDokResponse)
def create_jnsdok(payload: JnsDokCreate, uc: JnsDokUseCase = Depends(get_usecase)):
    return uc.create(
        payload.kddok,
        payload.namadok,
        payload.keterangan,
        payload.created_by,
        payload.updated_by,
    )


@router.get("/", response_model=list[JnsDokResponse])
def get_jnsdoks(uc: JnsDokUseCase = Depends(get_usecase)):
    return uc.get_all()


@router.get("/{kddok}", response_model=JnsDokResponse)
def get_jnsdok(kddok: str, uc: JnsDokUseCase = Depends(get_usecase)):
    jns_dok = uc.get_by_id(kddok)
    if not jns_dok:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="JnsDok not found")
    return jns_dok


@router.put("/{kddok}", response_model=JnsDokResponse)
def update_jnsdok(
    kddok: str,
    payload: JnsDokUpdate,
    uc: JnsDokUseCase = Depends(get_usecase),
):
    jns_dok = uc.update(
        kddok,
        payload.namadok,
        payload.keterangan,
        payload.updated_by,
    )
    if not jns_dok:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="JnsDok not found")
    return jns_dok


@router.delete("/{kddok}")
def delete_jnsdok(kddok: str, uc: JnsDokUseCase = Depends(get_usecase)):
    deleted = uc.delete(kddok)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="JnsDok not found")
    return {"message": "Deleted"}
