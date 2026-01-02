from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class MasterKabKotaAll:
    idkabkotaall: Optional[int]
    idprovinsi: int
    nmkabkota: str
    status: str
    kdkabkota: Optional[str] = None
    created_at: Optional[datetime] = None
    created_by: Optional[str] = None
    updated_at: Optional[datetime] = None
    updated_by: Optional[str] = None
