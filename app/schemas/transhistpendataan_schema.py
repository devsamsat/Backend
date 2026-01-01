from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel


class TransHistPendataanCreate(BaseModel):
    idpendataan: int
    spt: str
    idwpdata: int
    uruttgl: int
    tarifpjk: float
    idupt: int
    histid: str
    status: str
    tglpendataan: Optional[date] = None
    masaawal: Optional[date] = None
    masaakhir: Optional[date] = None
    jmlomzetawal: Optional[float] = None
    kdflow: Optional[str] = None
    created_by: Optional[str] = None
    updated_by: Optional[str] = None


class TransHistPendataanUpdate(BaseModel):
    idpendataan: Optional[int] = None
    spt: Optional[str] = None
    idwpdata: Optional[int] = None
    uruttgl: Optional[int] = None
    tarifpjk: Optional[float] = None
    idupt: Optional[int] = None
    histid: Optional[str] = None
    status: Optional[str] = None
    tglpendataan: Optional[date] = None
    masaawal: Optional[date] = None
    masaakhir: Optional[date] = None
    jmlomzetawal: Optional[float] = None
    kdflow: Optional[str] = None
    updated_by: Optional[str] = None


class TransHistPendataanResponse(BaseModel):
    idhistpendataan: int
    idpendataan: int
    spt: str
    idwpdata: int
    uruttgl: int
    tarifpjk: float
    idupt: int
    histid: str
    status: str
    tglpendataan: Optional[date]
    masaawal: Optional[date]
    masaakhir: Optional[date]
    jmlomzetawal: Optional[float]
    kdflow: Optional[str]
    created_at: datetime
    created_by: Optional[str]
    updated_at: datetime
    updated_by: Optional[str]

    class Config:
        from_attributes = True
