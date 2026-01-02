from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class JnsKendaraan:
    jnskendid: str
    jnskend: str
    katid: str
    jnsjrid: Optional[str] = None
    golpjr: Optional[int] = None
    golujr: Optional[int] = None
    created_at: Optional[datetime] = None
    created_by: Optional[str] = None
    updated_at: Optional[datetime] = None
    updated_by: Optional[str] = None
