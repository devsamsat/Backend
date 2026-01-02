from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class MasterRekd:
    idrekd: Optional[int]
    kdrek: str
    idparent: Optional[int] = None
    mtglevel: Optional[str] = None
    nmrek: Optional[str] = None
    kdjnspjk: Optional[str] = None
    rek_type: Optional[str] = None
    status: Optional[str] = None
    created_at: Optional[datetime] = None
    created_by: Optional[str] = None
    updated_at: Optional[datetime] = None
    updated_by: Optional[str] = None
