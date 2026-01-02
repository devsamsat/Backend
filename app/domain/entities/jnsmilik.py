from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class JnsMilik:
    kdmilik: str
    milik: str
    bpkpid: str
    status: Optional[str] = None
    created_at: Optional[datetime] = None
    created_by: Optional[str] = None
    updated_at: Optional[datetime] = None
    updated_by: Optional[str] = None
