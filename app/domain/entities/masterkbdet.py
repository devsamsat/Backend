from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class MasterKbDet:
    idkbdet: Optional[int]
    idkb: int
    idjnsd: int
    created_at: Optional[datetime] = None
    created_by: Optional[str] = None
    updated_at: Optional[datetime] = None
    updated_by: Optional[str] = None
