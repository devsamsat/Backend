from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.infrastructure.repositories.mapjnspendapatan_repository_impl import (
    MapJnsPendapatanRepositoryImpl,
)
from app.schemas.mapjnspendapatan_schema import (
    MapJnsPendapatanCreate,
    MapJnsPendapatanResponse,
    MapJnsPendapatanUpdate,
)
from app.usecases.mapjnspendapatan_usecase import MapJnsPendapatanUseCase

router = APIRouter(prefix="/api/v1/mapjnspendapatan", tags=["mapjnspendapatan"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_usecase(db: Session = Depends(get_db)):
    repo = MapJnsPendapatanRepositoryImpl(db)
    return MapJnsPendapatanUseCase(repo)


@router.post("/", response_model=MapJnsPendapatanResponse)
def create_mapjnspendapatan(
    payload: MapJnsPendapatanCreate,
    uc: MapJnsPendapatanUseCase = Depends(get_usecase),
):
    return uc.create(
        payload.nmjnspendapatan,
        payload.idrekpkb,
        payload.idrekbbnkb,
        payload.idrekopsenpkb,
        payload.idrekopsenbbnkb,
        payload.idrekpnbp,
        payload.keterangan,
        payload.created_by,
        payload.updated_by,
    )


@router.get("/", response_model=list[MapJnsPendapatanResponse])
def get_mapjnspendapatans(uc: MapJnsPendapatanUseCase = Depends(get_usecase)):
    return uc.get_all()


@router.get("/{idmapjnsd}", response_model=MapJnsPendapatanResponse)
def get_mapjnspendapatan(
    idmapjnsd: int,
    uc: MapJnsPendapatanUseCase = Depends(get_usecase),
):
    record = uc.get_by_id(idmapjnsd)
    if not record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MapJnsPendapatan not found",
        )
    return record


@router.put("/{idmapjnsd}", response_model=MapJnsPendapatanResponse)
def update_mapjnspendapatan(
    idmapjnsd: int,
    payload: MapJnsPendapatanUpdate,
    uc: MapJnsPendapatanUseCase = Depends(get_usecase),
):
    record = uc.update(
        idmapjnsd,
        payload.nmjnspendapatan,
        payload.idrekpkb,
        payload.idrekbbnkb,
        payload.idrekopsenpkb,
        payload.idrekopsenbbnkb,
        payload.idrekpnbp,
        payload.keterangan,
        payload.updated_by,
    )
    if not record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MapJnsPendapatan not found",
        )
    return record


@router.delete("/{idmapjnsd}")
def delete_mapjnspendapatan(
    idmapjnsd: int,
    uc: MapJnsPendapatanUseCase = Depends(get_usecase),
):
    deleted = uc.delete(idmapjnsd)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="MapJnsPendapatan not found",
        )
    return {"message": "Deleted"}
