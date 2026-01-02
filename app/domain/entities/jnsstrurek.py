from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class JnsStruRek:
    mtglevel: str
    nmlevel: str
    keterangan: str
    created_at: Optional[datetime] = None
    created_by: Optional[str] = None
    updated_at: Optional[datetime] = None
    updated_by: Optional[str] = None
