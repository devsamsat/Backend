from dataclasses import dataclass
from datetime import date, datetime
from typing import Optional


@dataclass
class TransSts:
    idsts: Optional[int]
    idupt: int
    idbend: int
    nosts: str
    keterangan: str
    statbayar: str
    setorandari: Optional[str] = None
    tglsts: Optional[date] = None
    ntpd: Optional[str] = None
    tglntpd: Optional[date] = None
    statsts: Optional[int] = None
    created_at: Optional[datetime] = None
    created_by: Optional[str] = None
    updated_at: Optional[datetime] = None
    updated_by: Optional[str] = None
