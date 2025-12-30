from datetime import date, datetime
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel


class MasterHapusDendaCreate(BaseModel):
    jenis: str
    uraian: str
    awal: Optional[date] = None
    akhir: Optional[date] = None
    nilai: Optional[Decimal] = None
    satuan: Optional[str] = None
    ket: Optional[str] = None
    status: Optional[str] = None
    created_by: Optional[str] = None
    updated_by: Optional[str] = None


class MasterHapusDendaUpdate(BaseModel):
    jenis: Optional[str] = None
    uraian: Optional[str] = None
    awal: Optional[date] = None
    akhir: Optional[date] = None
    nilai: Optional[Decimal] = None
    satuan: Optional[str] = None
    ket: Optional[str] = None
    status: Optional[str] = None
    updated_by: Optional[str] = None


class MasterHapusDendaResponse(BaseModel):
    idhapusdenda: int
    jenis: str
    uraian: str
    awal: Optional[date]
    akhir: Optional[date]
    nilai: Optional[Decimal]
    satuan: Optional[str]
    ket: Optional[str]
    status: Optional[str]
    created_at: datetime
    created_by: Optional[str]
    updated_at: datetime
    updated_by: Optional[str]

    class Config:
        from_attributes = True
