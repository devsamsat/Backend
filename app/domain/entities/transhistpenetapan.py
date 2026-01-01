from dataclasses import dataclass
from datetime import date, datetime
from typing import Optional


@dataclass
class TransHistPenetapan:
    idhistpenetapan: Optional[int] = None
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
    created_at: Optional[datetime] = None
    created_by: Optional[str] = None
    updated_at: Optional[datetime] = None
    updated_by: Optional[str] = None
