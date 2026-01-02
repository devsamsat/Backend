from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class MapJnsPendapatanCreate(BaseModel):
    nmjnspendapatan: str
    idrekpkb: Optional[int] = None
    idrekbbnkb: Optional[int] = None
    idrekopsenpkb: Optional[int] = None
    idrekopsenbbnkb: Optional[int] = None
    idrekpnbp: Optional[int] = None
    keterangan: Optional[str] = None
    created_by: Optional[str] = None
    updated_by: Optional[str] = None


class MapJnsPendapatanUpdate(BaseModel):
    nmjnspendapatan: Optional[str] = None
    idrekpkb: Optional[int] = None
    idrekbbnkb: Optional[int] = None
    idrekopsenpkb: Optional[int] = None
    idrekopsenbbnkb: Optional[int] = None
    idrekpnbp: Optional[int] = None
    keterangan: Optional[str] = None
    updated_by: Optional[str] = None


class MapJnsPendapatanResponse(BaseModel):
    idmapjnsd: int
    nmjnspendapatan: str
    idrekpkb: Optional[int]
    idrekbbnkb: Optional[int]
    idrekopsenpkb: Optional[int]
    idrekopsenbbnkb: Optional[int]
    idrekpnbp: Optional[int]
    keterangan: Optional[str]
    created_at: datetime
    created_by: Optional[str]
    updated_at: datetime
    updated_by: Optional[str]

    class Config:
        from_attributes = True
