from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel


class MasterLiburCreate(BaseModel):
    idkabkota: int
    level: str
    tanggal: Optional[date] = None
    namalibur: Optional[str] = None
    keterangan: Optional[str] = None
    created_by: Optional[str] = None
    updated_by: Optional[str] = None


class MasterLiburUpdate(BaseModel):
    idkabkota: Optional[int] = None
    level: Optional[str] = None
    tanggal: Optional[date] = None
    namalibur: Optional[str] = None
    keterangan: Optional[str] = None
    updated_by: Optional[str] = None


class MasterLiburResponse(BaseModel):
    idlibur: int
    idkabkota: int
    level: str
    tanggal: Optional[date]
    namalibur: Optional[str]
    keterangan: Optional[str]
    created_at: datetime
    created_by: Optional[str]
    updated_at: datetime
    updated_by: Optional[str]

    class Config:
        from_attributes = True
