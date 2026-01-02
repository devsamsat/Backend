from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.infrastructure.repositories.jnsplat_repository_impl import JnsPlatRepositoryImpl
from app.schemas.jnsplat_schema import JnsPlatCreate, JnsPlatResponse, JnsPlatUpdate
from app.usecases.jnsplat_usecase import JnsPlatUseCase

router = APIRouter(prefix="/api/v1/jnsplat", tags=["JnsPlat"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_usecase(db: Session = Depends(get_db)):
    repo = JnsPlatRepositoryImpl(db)
    return JnsPlatUseCase(repo)


@router.post("/", response_model=JnsPlatResponse)
def create_jnsplat(payload: JnsPlatCreate, uc: JnsPlatUseCase = Depends(get_usecase)):
    return uc.create(
        payload.kdplat,
        payload.plat,
        payload.pu,
        payload.platjr,
        payload.numpkb,
        payload.numbbn1,
        payload.numbbn2,
        payload.umorg,
        payload.umbrg,
        payload.dnumpkb,
        payload.dnumbbn,
        payload.dumorg,
        payload.dumbrg,
        payload.abpkb,
        payload.abbbn1,
        payload.abbbn2,
        payload.numfiskal,
        payload.snid,
        payload.opspkb,
        payload.opsbbn,
        payload.opsnumpkb,
        payload.opsnumbbn1,
        payload.opsnumbbn2,
        payload.opsdnumpkb,
        payload.opsdnumbbn,
        payload.minnumpkb,
        payload.minnumbbn1,
        payload.minnumbbn2,
        payload.created_by,
        payload.updated_by,
    )


@router.get("/", response_model=list[JnsPlatResponse])
def get_jnsplats(uc: JnsPlatUseCase = Depends(get_usecase)):
    return uc.get_all()


@router.get("/{kdplat}", response_model=JnsPlatResponse)
def get_jnsplat(kdplat: str, uc: JnsPlatUseCase = Depends(get_usecase)):
    jns_plat = uc.get_by_id(kdplat)
    if not jns_plat:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="JnsPlat not found")
    return jns_plat


@router.put("/{kdplat}", response_model=JnsPlatResponse)
def update_jnsplat(
    kdplat: str,
    payload: JnsPlatUpdate,
    uc: JnsPlatUseCase = Depends(get_usecase),
):
    jns_plat = uc.update(
        kdplat,
        payload.plat,
        payload.pu,
        payload.platjr,
        payload.numpkb,
        payload.numbbn1,
        payload.numbbn2,
        payload.umorg,
        payload.umbrg,
        payload.dnumpkb,
        payload.dnumbbn,
        payload.dumorg,
        payload.dumbrg,
        payload.abpkb,
        payload.abbbn1,
        payload.abbbn2,
        payload.numfiskal,
        payload.snid,
        payload.opspkb,
        payload.opsbbn,
        payload.opsnumpkb,
        payload.opsnumbbn1,
        payload.opsnumbbn2,
        payload.opsdnumpkb,
        payload.opsdnumbbn,
        payload.minnumpkb,
        payload.minnumbbn1,
        payload.minnumbbn2,
        payload.updated_by,
    )
    if not jns_plat:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="JnsPlat not found")
    return jns_plat


@router.delete("/{kdplat}")
def delete_jnsplat(kdplat: str, uc: JnsPlatUseCase = Depends(get_usecase)):
    deleted = uc.delete(kdplat)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="JnsPlat not found")
    return {"message": "Deleted"}
