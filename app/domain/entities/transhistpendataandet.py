from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from typing import Optional


@dataclass
class TransHistPendataanDet:
    idhistpendataandet: Optional[int]
    idhistpendataan: int
    idpenetapan: int
    nourut: int
    transid: str
    ket1: str
    usahaid: int
    tarifpajak: Decimal
    histid: str
    status: str
    lokasi: Optional[str] = None
    created_at: Optional[datetime] = None
    created_by: Optional[str] = None
    updated_at: Optional[datetime] = None
    updated_by: Optional[str] = None
