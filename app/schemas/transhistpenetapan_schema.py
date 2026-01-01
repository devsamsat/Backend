from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel


class TransHistPenetapanCreate(BaseModel):
    idpenetapan: int
    idkohir: int
    idwpdata: int
    uruttgl: int
    tarifpajak: float
    statbayar: str
    status: str
    nokohir: Optional[str] = None
    tglpenetapan: Optional[date] = None
    tgljatuhtempo: Optional[date] = None
    masaawal: Optional[date] = None
    masaakhir: Optional[date] = None
    jmlomzetawal: Optional[float] = None
    denda: Optional[float] = None
    kenaikan: Optional[float] = None
    tglbayar: Optional[date] = None
    jmlbayar: Optional[float] = None
    tglkurangbayar: Optional[date] = None
    jmlkurangbayar: Optional[float] = None
    jmlperingatan: Optional[int] = None
    kdflow: Optional[str] = None
    opsid: Optional[str] = None
    opsprov: Optional[float] = None
    opskota: Optional[float] = None
    dendaopsprov: Optional[float] = None
    dendaopskota: Optional[float] = None
    created_by: Optional[str] = None
    updated_by: Optional[str] = None


class TransHistPenetapanUpdate(BaseModel):
    idpenetapan: Optional[int] = None
    idkohir: Optional[int] = None
    idwpdata: Optional[int] = None
    uruttgl: Optional[int] = None
    tarifpajak: Optional[float] = None
    statbayar: Optional[str] = None
    status: Optional[str] = None
    nokohir: Optional[str] = None
    tglpenetapan: Optional[date] = None
    tgljatuhtempo: Optional[date] = None
    masaawal: Optional[date] = None
    masaakhir: Optional[date] = None
    jmlomzetawal: Optional[float] = None
    denda: Optional[float] = None
    kenaikan: Optional[float] = None
    tglbayar: Optional[date] = None
    jmlbayar: Optional[float] = None
    tglkurangbayar: Optional[date] = None
    jmlkurangbayar: Optional[float] = None
    jmlperingatan: Optional[int] = None
    kdflow: Optional[str] = None
    opsid: Optional[str] = None
    opsprov: Optional[float] = None
    opskota: Optional[float] = None
    dendaopsprov: Optional[float] = None
    dendaopskota: Optional[float] = None
    updated_by: Optional[str] = None


class TransHistPenetapanResponse(BaseModel):
    idhistpenetapan: int
    idpenetapan: int
    idkohir: int
    idwpdata: int
    uruttgl: int
    tarifpajak: float
    statbayar: str
    status: str
    nokohir: Optional[str]
    tglpenetapan: Optional[date]
    tgljatuhtempo: Optional[date]
    masaawal: Optional[date]
    masaakhir: Optional[date]
    jmlomzetawal: Optional[float]
    denda: Optional[float]
    kenaikan: Optional[float]
    tglbayar: Optional[date]
    jmlbayar: Optional[float]
    tglkurangbayar: Optional[date]
    jmlkurangbayar: Optional[float]
    jmlperingatan: Optional[int]
    kdflow: Optional[str]
    opsid: Optional[str]
    opsprov: Optional[float]
    opskota: Optional[float]
    dendaopsprov: Optional[float]
    dendaopskota: Optional[float]
    created_at: datetime
    created_by: Optional[str]
    updated_at: datetime
    updated_by: Optional[str]

    class Config:
        from_attributes = True
