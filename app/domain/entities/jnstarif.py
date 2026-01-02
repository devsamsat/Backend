from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class JnsTarif:
    kdjnstarif: str
    nmjnstarif: str
    idupt: int
    jnskendid: Optional[str] = None
    idrekd: Optional[int] = None
    status: Optional[str] = None
    created_at: Optional[datetime] = None
    created_by: Optional[str] = None
    updated_at: Optional[datetime] = None
    updated_by: Optional[str] = None
