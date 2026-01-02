from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class JnsProgresif:
    kdprogresif: int
    progresifr2: float
    progresifr4: float
    created_at: Optional[datetime] = None
    created_by: Optional[str] = None
    updated_at: Optional[datetime] = None
    updated_by: Optional[str] = None
