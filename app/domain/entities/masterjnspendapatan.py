from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class MasterJnsPendapatan:
    idjnsd: Optional[int]
    nmjnspendapatan: str
    parentid: Optional[int] = None
    kdrek: Optional[str] = None
    jatuhtempo: Optional[int] = None
    status: Optional[str] = None
    selfassessment: Optional[str] = None
    katid: Optional[str] = None
    created_at: Optional[datetime] = None
    created_by: Optional[str] = None
    updated_at: Optional[datetime] = None
    updated_by: Optional[str] = None
