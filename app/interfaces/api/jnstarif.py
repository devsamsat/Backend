from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.infrastructure.repositories.jnstarif_repository_impl import JnsTarifRepositoryImpl
from app.schemas.jnstarif_schema import (
    JnsTarifCreate,
    JnsTarifResponse,
    JnsTarifUpdate,
)
from app.usecases.jnstarif_usecase import JnsTarifUseCase

router = APIRouter(prefix="/api/v1/jnstarif", tags=["jnstarif"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_usecase(db: Session = Depends(get_db)):
    repo = JnsTarifRepositoryImpl(db)
    return JnsTarifUseCase(repo)


@router.post("/", response_model=JnsTarifResponse)
def create_jnstarif(
    payload: JnsTarifCreate,
    uc: JnsTarifUseCase = Depends(get_usecase),
):
    return uc.create(
        payload.kdjnstarif,
        payload.nmjnstarif,
        payload.idupt,
        payload.jnskendid,
        payload.idrekd,
        payload.status,
        payload.created_by,
        payload.updated_by,
    )


@router.get("/", response_model=list[JnsTarifResponse])
def get_jnstarifs(uc: JnsTarifUseCase = Depends(get_usecase)):
    return uc.get_all()


@router.get("/{kdjnstarif}", response_model=JnsTarifResponse)
def get_jnstarif(kdjnstarif: str, uc: JnsTarifUseCase = Depends(get_usecase)):
    record = uc.get_by_id(kdjnstarif)
    if not record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="JnsTarif not found",
        )
    return record


@router.put("/{kdjnstarif}", response_model=JnsTarifResponse)
def update_jnstarif(
    kdjnstarif: str,
    payload: JnsTarifUpdate,
    uc: JnsTarifUseCase = Depends(get_usecase),
):
    record = uc.update(
        kdjnstarif,
        payload.nmjnstarif,
        payload.idupt,
        payload.jnskendid,
        payload.idrekd,
        payload.status,
        payload.updated_by,
    )
    if not record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="JnsTarif not found",
        )
    return record


@router.delete("/{kdjnstarif}")
def delete_jnstarif(kdjnstarif: str, uc: JnsTarifUseCase = Depends(get_usecase)):
    deleted = uc.delete(kdjnstarif)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="JnsTarif not found",
        )
    return {"message": "Deleted"}
