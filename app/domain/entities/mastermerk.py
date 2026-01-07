from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class MasterMerk:
    idmerk: Optional[int]
    nmmerk: str
    kdmerk: Optional[str] = None
    keterangan: Optional[str] = None
    status: Optional[str] = None
    created_at: Optional[datetime] = None
    created_by: Optional[str] = None
    updated_at: Optional[datetime] = None
    updated_by: Optional[str] = None
