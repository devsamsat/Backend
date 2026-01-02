from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class TransWpDataAntri:
    idantri: Optional[int]
    idtwpdata: int
    noantri: str
    idktp: Optional[int] = None
    statantri: Optional[str] = None
    ket: Optional[str] = None
    tglantri: Optional[str] = None
    created_at: Optional[datetime] = None
    created_by: Optional[str] = None
    updated_at: Optional[datetime] = None
    updated_by: Optional[str] = None
