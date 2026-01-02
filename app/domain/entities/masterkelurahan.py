from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class MasterKelurahan:
    idkelurahan: Optional[int]
    idkecamatan: int
    nmkelurahan: str
    alamat: str
    telepon: str
    status: str
    kdkelurahan: Optional[str] = None
    kodepos: Optional[str] = None
    created_at: Optional[datetime] = None
    created_by: Optional[str] = None
    updated_at: Optional[datetime] = None
    updated_by: Optional[str] = None
