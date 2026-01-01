from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class MasterUuNjop:
    iduunjop: Optional[int] = None
    noperkada: Optional[str] = None
    isiperkada: Optional[str] = None
    tahun: Optional[str] = None
    status: Optional[str] = None
    keterangan: Optional[str] = None
    created_at: Optional[datetime] = None
    created_by: Optional[str] = None
    updated_at: Optional[datetime] = None
    updated_by: Optional[str] = None
