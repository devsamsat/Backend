from dataclasses import dataclass
from datetime import date, datetime
from typing import Optional


@dataclass
class MasterWpData:
    idwpdata: Optional[int]
    idjnsd: int
    idwp: int
    tglpendataan: Optional[date] = None
    created_at: Optional[datetime] = None
    created_by: Optional[str] = None
    updated_at: Optional[datetime] = None
    updated_by: Optional[str] = None
