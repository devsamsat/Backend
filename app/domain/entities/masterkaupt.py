from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class MasterKaupt:
    idkaupt: Optional[int]
    idupt: int
    idpegawai: Optional[int] = None
    created_at: Optional[datetime] = None
    created_by: Optional[str] = None
    updated_at: Optional[datetime] = None
    updated_by: Optional[str] = None
