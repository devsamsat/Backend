from datetime import date, datetime
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel


class TransHistPenetapanCreate(BaseModel):
    idpenetapan: int
    idkohir: int
    idwpdata: int
    uruttgl: int
    tarifpajak: Decimal
    statbayar: str
    status: str
    nokohir: Optional[str] = None
    tglpenetapan: Optional[date] = None
    tgljatuhtempo: Optional[date] = None
    masaawal: Optional[date] = None
    masaakhir: Optional[date] = None
    jmlomzetawal: Optional[Decimal] = None
    denda: Optional[Decimal] = None
    kenaikan: Optional[Decimal] = None
    tglbayar: Optional[date] = None
    jmlbayar: Optional[Decimal] = None
    tglkurangbayar: Optional[date] = None
    jmlkurangbayar: Optional[Decimal] = None
    jmlperingatan: Optional[int] = None
    kdflow: Optional[str] = None
    opsid: Optional[str] = None
    opsprov: Optional[Decimal] = None
    opskota: Optional[Decimal] = None
    dendaopsprov: Optional[Decimal] = None
    dendaopskota: Optional[Decimal] = None
    created_by: Optional[str] = None
    updated_by: Optional[str] = None


class TransHistPenetapanUpdate(BaseModel):
    idpenetapan: Optional[int] = None
    idkohir: Optional[int] = None
    idwpdata: Optional[int] = None
    uruttgl: Optional[int] = None
    tarifpajak: Optional[Decimal] = None
    statbayar: Optional[str] = None
    status: Optional[str] = None
    nokohir: Optional[str] = None
    tglpenetapan: Optional[date] = None
    tgljatuhtempo: Optional[date] = None
    masaawal: Optional[date] = None
    masaakhir: Optional[date] = None
    jmlomzetawal: Optional[Decimal] = None
    denda: Optional[Decimal] = None
    kenaikan: Optional[Decimal] = None
    tglbayar: Optional[date] = None
    jmlbayar: Optional[Decimal] = None
    tglkurangbayar: Optional[date] = None
    jmlkurangbayar: Optional[Decimal] = None
    jmlperingatan: Optional[int] = None
    kdflow: Optional[str] = None
    opsid: Optional[str] = None
    opsprov: Optional[Decimal] = None
    opskota: Optional[Decimal] = None
    dendaopsprov: Optional[Decimal] = None
    dendaopskota: Optional[Decimal] = None
    updated_by: Optional[str] = None


class TransHistPenetapanResponse(BaseModel):
    idhistpenetapan: int
    idpenetapan: int
    idkohir: int
    idwpdata: int
    uruttgl: int
    tarifpajak: Decimal
    statbayar: str
    status: str
    nokohir: Optional[str]
    tglpenetapan: Optional[date]
    tgljatuhtempo: Optional[date]
    masaawal: Optional[date]
    masaakhir: Optional[date]
    jmlomzetawal: Optional[Decimal]
    denda: Optional[Decimal]
    kenaikan: Optional[Decimal]
    tglbayar: Optional[date]
    jmlbayar: Optional[Decimal]
    tglkurangbayar: Optional[date]
    jmlkurangbayar: Optional[Decimal]
    jmlperingatan: Optional[int]
    kdflow: Optional[str]
    opsid: Optional[str]
    opsprov: Optional[Decimal]
    opskota: Optional[Decimal]
    dendaopsprov: Optional[Decimal]
    dendaopskota: Optional[Decimal]
    created_at: datetime
    created_by: Optional[str]
    updated_at: datetime
    updated_by: Optional[str]

    class Config:
        from_attributes = True
