from dataclasses import dataclass
from datetime import date, datetime
from decimal import Decimal
from typing import Optional


@dataclass
class TransHistPendataan:
    idhistpendataan: Optional[int]
    idpendataan: int
    spt: str
    idwpdata: int
    uruttgl: int
    tarifpjk: Decimal
    idupt: int
    histid: str
    status: str
    tglpendataan: Optional[date] = None
    masaawal: Optional[date] = None
    masaakhir: Optional[date] = None
    jmlomzetawal: Optional[Decimal] = None
    kdflow: Optional[str] = None
    created_at: Optional[datetime] = None
    created_by: Optional[str] = None
    updated_at: Optional[datetime] = None
    updated_by: Optional[str] = None
