from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from decimal import Decimal


@dataclass
class JnsGuna:
    kdguna: str
    guna: str
    gunaplat: Optional[str]
    progresif: Optional[Decimal]
    groupbpkb: str
    created_at: Optional[datetime] = None
    created_by: Optional[str] = None
    updated_at: Optional[datetime] = None
    updated_by: Optional[str] = None
