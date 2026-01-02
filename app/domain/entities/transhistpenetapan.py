from dataclasses import dataclass
from datetime import date, datetime
from decimal import Decimal
from typing import Optional


@dataclass
class TransHistPenetapan:
    idhistpenetapan: Optional[int]
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
    created_at: Optional[datetime] = None
    created_by: Optional[str] = None
    updated_at: Optional[datetime] = None
    updated_by: Optional[str] = None
