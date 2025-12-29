from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class JnsGuna:
    kdguna: str
    guna: str
    gunaplat: Optional[str] = None
    progresif: Optional[float] = None
    groupbpkb: Optional[str] = None
    created_at: Optional[datetime] = None
    created_by: Optional[str] = None
    updated_at: Optional[datetime] = None
    updated_by: Optional[str] = None
