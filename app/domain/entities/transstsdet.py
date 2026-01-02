from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from typing import Optional


@dataclass
class TransStsDet:
    idstsdet: Optional[int]
    idsts: int
    idrekd: int
    nilaists: Decimal
    jenis: str
    created_at: Optional[datetime] = None
    created_by: Optional[str] = None
    updated_at: Optional[datetime] = None
    updated_by: Optional[str] = None
