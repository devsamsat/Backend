from dataclasses import dataclass
from datetime import date, datetime
from typing import Optional


@dataclass
class MasterLibur:
    idlibur: Optional[int]
    idkabkota: int
    level: str
    tanggal: Optional[date] = None
    namalibur: Optional[str] = None
    keterangan: Optional[str] = None
    created_at: Optional[datetime] = None
    created_by: Optional[str] = None
    updated_at: Optional[datetime] = None
    updated_by: Optional[str] = None
