from dataclasses import dataclass
from datetime import date, datetime
from typing import Optional


@dataclass
class TransWpData:
    idtwpdata: Optional[int]
    idnpwpd: int
    kdflow: Optional[str] = None
    tgldaftar: Optional[date] = None
    created_at: Optional[datetime] = None
    created_by: Optional[str] = None
    updated_at: Optional[datetime] = None
    updated_by: Optional[str] = None
