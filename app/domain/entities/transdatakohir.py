from dataclasses import dataclass
from datetime import date, datetime
from typing import Optional


@dataclass
class TransDataKohir:
    idkohir: Optional[int] = None
    penagih: str
    idwp: int
    masaawal: Optional[date] = None
    masaakhir: Optional[date] = None
    tglpenetapan: Optional[date] = None
    tglkurangbayar: Optional[date] = None
    keterangan: Optional[str] = None
    idupt: Optional[int] = None
    skrupt: Optional[str] = None
    validjr: Optional[str] = None
    validjrby: Optional[str] = None
    validpol: Optional[str] = None
    validpolby: Optional[str] = None
    ntpd: Optional[str] = None
    tglntpd: Optional[date] = None
    idbank: Optional[str] = None
    created_at: Optional[datetime] = None
    created_by: Optional[str] = None
    updated_at: Optional[datetime] = None
    updated_by: Optional[str] = None
