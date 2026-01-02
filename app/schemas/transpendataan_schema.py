from datetime import date, datetime
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel


class TransPendataanCreate(BaseModel):
    spt: str
    idwpdata: int
    uruttgl: int
    tarifpjk: Decimal
    idupt: int
    status: str
    tglpendataan: Optional[date] = None
    masaawal: Optional[date] = None
    masaakhir: Optional[date] = None
    jmlomzetawal: Optional[Decimal] = None
    kdflow: Optional[str] = None
    created_by: Optional[str] = None
    updated_by: Optional[str] = None


class TransPendataanUpdate(BaseModel):
    spt: Optional[str] = None
    idwpdata: Optional[int] = None
    uruttgl: Optional[int] = None
    tarifpjk: Optional[Decimal] = None
    idupt: Optional[int] = None
    status: Optional[str] = None
    tglpendataan: Optional[date] = None
    masaawal: Optional[date] = None
    masaakhir: Optional[date] = None
    jmlomzetawal: Optional[Decimal] = None
    kdflow: Optional[str] = None
    updated_by: Optional[str] = None


class TransPendataanResponse(BaseModel):
    idpendataan: int
    spt: str
    idwpdata: int
    uruttgl: int
    tarifpjk: Decimal
    idupt: int
    status: str
    tglpendataan: Optional[date]
    masaawal: Optional[date]
    masaakhir: Optional[date]
    jmlomzetawal: Optional[Decimal]
    kdflow: Optional[str]
    created_at: datetime
    created_by: Optional[str]
    updated_at: datetime
    updated_by: Optional[str]

    class Config:
        from_attributes = True
