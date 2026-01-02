from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class MasterKiosk:
    idkios: Optional[int]
    kodekiosk: str
    datakiosk: str
    level: str
    status: str
    idparent: Optional[int] = None
    created_at: Optional[datetime] = None
    created_by: Optional[str] = None
    updated_at: Optional[datetime] = None
    updated_by: Optional[str] = None
