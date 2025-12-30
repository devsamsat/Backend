from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class MasterJabTtd:
    idjabttd: Optional[int]
    idpegawai: int
    kddok: str
    jabatan: Optional[str] = None
    ket: Optional[str] = None
    status: Optional[str] = None
    created_at: Optional[datetime] = None
    created_by: Optional[str] = None
    updated_at: Optional[datetime] = None
    updated_by: Optional[str] = None
