from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.infrastructure.repositories.jnspajak_repository_impl import JnsPajakRepositoryImpl
from app.schemas.jnspajak_schema import JnsPajakCreate, JnsPajakResponse, JnsPajakUpdate
from app.usecases.jnspajak_usecase import JnsPajakUseCase

router = APIRouter(prefix="/api/v1/jnspajak", tags=["JnsPajak"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_usecase(db: Session = Depends(get_db)):
    repo = JnsPajakRepositoryImpl(db)
    return JnsPajakUseCase(repo)


@router.post("/", response_model=JnsPajakResponse)
def create_jnspajak(payload: JnsPajakCreate, uc: JnsPajakUseCase = Depends(get_usecase)):
    return uc.create(
        payload.kdjnspjk,
        payload.nmjnspjk,
        payload.keterangan,
        payload.created_by,
        payload.updated_by,
    )


@router.get("/", response_model=list[JnsPajakResponse])
def get_jnspajaks(uc: JnsPajakUseCase = Depends(get_usecase)):
    return uc.get_all()


@router.get("/{kdjnspjk}", response_model=JnsPajakResponse)
def get_jnspajak(kdjnspjk: str, uc: JnsPajakUseCase = Depends(get_usecase)):
    jns_pajak = uc.get_by_id(kdjnspjk)
    if not jns_pajak:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="JnsPajak not found")
    return jns_pajak


@router.put("/{kdjnspjk}", response_model=JnsPajakResponse)
def update_jnspajak(
    kdjnspjk: str,
    payload: JnsPajakUpdate,
    uc: JnsPajakUseCase = Depends(get_usecase),
):
    jns_pajak = uc.update(
        kdjnspjk,
        payload.nmjnspjk,
        payload.keterangan,
        payload.updated_by,
    )
    if not jns_pajak:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="JnsPajak not found")
    return jns_pajak


@router.delete("/{kdjnspjk}")
def delete_jnspajak(kdjnspjk: str, uc: JnsPajakUseCase = Depends(get_usecase)):
    deleted = uc.delete(kdjnspjk)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="JnsPajak not found")
    return {"message": "Deleted"}
