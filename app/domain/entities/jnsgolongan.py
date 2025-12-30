from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class JnsGolongan:
    jnsgolid: str
    golongan: str
    katid: Optional[str]
    jnskendid: Optional[str]
    viewall: Optional[str]
    status: Optional[str]
    created_at: Optional[datetime] = None
    created_by: Optional[str] = None
    updated_at: Optional[datetime] = None
    updated_by: Optional[str] = None
