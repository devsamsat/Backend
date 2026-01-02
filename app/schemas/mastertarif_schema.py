from datetime import datetime
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel


class MasterTarifCreate(BaseModel):
    kdjnspjk: str
    jnskendid: Optional[str] = None
    satuan: Optional[str] = None
    awal: Optional[Decimal] = None
    akhir: Optional[Decimal] = None
    keterangan: Optional[str] = None
    kdflow: Optional[str] = None
    kdplat: Optional[str] = None
    statumum: Optional[str] = None
    tarif: Optional[Decimal] = None
    created_by: Optional[str] = None
    updated_by: Optional[str] = None


class MasterTarifUpdate(BaseModel):
    kdjnspjk: Optional[str] = None
    jnskendid: Optional[str] = None
    satuan: Optional[str] = None
    awal: Optional[Decimal] = None
    akhir: Optional[Decimal] = None
    keterangan: Optional[str] = None
    kdflow: Optional[str] = None
    kdplat: Optional[str] = None
    statumum: Optional[str] = None
    tarif: Optional[Decimal] = None
    updated_by: Optional[str] = None


class MasterTarifResponse(BaseModel):
    idtarif: int
    kdjnspjk: str
    jnskendid: Optional[str]
    satuan: Optional[str]
    awal: Optional[Decimal]
    akhir: Optional[Decimal]
    keterangan: Optional[str]
    kdflow: Optional[str]
    kdplat: Optional[str]
    statumum: Optional[str]
    tarif: Optional[Decimal]
    created_at: datetime
    created_by: Optional[str]
    updated_at: datetime
    updated_by: Optional[str]

    class Config:
        from_attributes = True
