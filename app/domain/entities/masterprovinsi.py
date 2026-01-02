from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class MasterProvinsi:
    idprovinsi: Optional[int]
    kdprovinsi: str
    nmprovinsi: str
    status: str
    created_at: Optional[datetime] = None
    created_by: Optional[str] = None
    updated_at: Optional[datetime] = None
    updated_by: Optional[str] = None
