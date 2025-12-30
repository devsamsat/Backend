from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class MasterBank:
    idbank: Optional[int]
    kodebank: str
    namabank: str
    akronimbank: Optional[str] = None
    cabangbank: Optional[str] = None
    alamatbank: Optional[str] = None
    status: Optional[str] = None
    created_at: Optional[datetime] = None
    created_by: Optional[str] = None
    updated_at: Optional[datetime] = None
    updated_by: Optional[str] = None
