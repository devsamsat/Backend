from dataclasses import dataclass
from datetime import date, datetime
from decimal import Decimal
from typing import Optional


@dataclass
class MasterHapusDenda:
    idhapusdenda: Optional[int]
    jenis: str
    uraian: str
    awal: Optional[date] = None
    akhir: Optional[date] = None
    nilai: Optional[Decimal] = None
    satuan: Optional[str] = None
    ket: Optional[str] = None
    status: Optional[str] = None
    created_at: Optional[datetime] = None
    created_by: Optional[str] = None
    updated_at: Optional[datetime] = None
    updated_by: Optional[str] = None
