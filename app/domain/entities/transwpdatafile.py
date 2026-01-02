from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class TransWpDataFile:
    idfile: Optional[int]
    idtwpdata: int
    namafile: Optional[str] = None
    direktory: Optional[str] = None
    extension: Optional[str] = None
    size: Optional[int] = None
    url: Optional[str] = None
    created_at: Optional[datetime] = None
    created_by: Optional[str] = None
    updated_at: Optional[datetime] = None
    updated_by: Optional[str] = None
