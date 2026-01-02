from dataclasses import dataclass
from datetime import date, datetime
from decimal import Decimal
from typing import Optional


@dataclass
class TransPendataan:
    idpendataan: Optional[int]
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
    created_at: Optional[datetime] = None
    created_by: Optional[str] = None
    updated_at: Optional[datetime] = None
    updated_by: Optional[str] = None
