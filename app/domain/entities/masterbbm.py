from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class MasterBbm:
    kodebbm: str
    namabbm: str
    keterangan: Optional[str] = None
    created_at: Optional[datetime] = None
    created_by: Optional[str] = None
    updated_at: Optional[datetime] = None
    updated_by: Optional[str] = None
