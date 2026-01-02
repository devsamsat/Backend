from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class MapJnsPendapatan:
    idmapjnsd: Optional[int]
    nmjnspendapatan: str
    idrekpkb: Optional[int] = None
    idrekbbnkb: Optional[int] = None
    idrekopsenpkb: Optional[int] = None
    idrekopsenbbnkb: Optional[int] = None
    idrekpnbp: Optional[int] = None
    keterangan: Optional[str] = None
    created_at: Optional[datetime] = None
    created_by: Optional[str] = None
    updated_at: Optional[datetime] = None
    updated_by: Optional[str] = None
