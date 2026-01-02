from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class MasterKecamatan:
    idkecamatan: Optional[int]
    idkabkota: int
    nmkecamatan: str
    alamat: str
    telepon: str
    status: str
    kdkecamatan: Optional[str] = None
    fax: Optional[str] = None
    created_at: Optional[datetime] = None
    created_by: Optional[str] = None
    updated_at: Optional[datetime] = None
    updated_by: Optional[str] = None
