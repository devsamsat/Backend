from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class MasterKabKota:
    idkabkota: Optional[int]
    idprovinsi: int
    nmkabkota: str
    akronim: str
    ibukota: str
    status: str
    bpkbid: str
    kdkabkota: Optional[str] = None
    created_at: Optional[datetime] = None
    created_by: Optional[str] = None
    updated_at: Optional[datetime] = None
    updated_by: Optional[str] = None
