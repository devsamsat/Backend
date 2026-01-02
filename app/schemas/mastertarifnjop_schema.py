from datetime import datetime
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel


class MasterTarifNjopCreate(BaseModel):
    iduunjop: int
    idrekd: Optional[int] = None
    kdjnstarif: Optional[str] = None
    namatarif: Optional[str] = None
    idmerk: Optional[int] = None
    tipe: Optional[str] = None
    silinder: Optional[str] = None
    tahun: Optional[str] = None
    kodebbm: Optional[str] = None
    njop: Optional[Decimal] = None
    status: Optional[str] = None
    created_by: Optional[str] = None
    updated_by: Optional[str] = None


class MasterTarifNjopUpdate(BaseModel):
    iduunjop: Optional[int] = None
    idrekd: Optional[int] = None
    kdjnstarif: Optional[str] = None
    namatarif: Optional[str] = None
    idmerk: Optional[int] = None
    tipe: Optional[str] = None
    silinder: Optional[str] = None
    tahun: Optional[str] = None
    kodebbm: Optional[str] = None
    njop: Optional[Decimal] = None
    status: Optional[str] = None
    updated_by: Optional[str] = None


class MasterTarifNjopResponse(BaseModel):
    idtarifnjop: int
    iduunjop: int
    idrekd: Optional[int]
    kdjnstarif: Optional[str]
    namatarif: Optional[str]
    idmerk: Optional[int]
    tipe: Optional[str]
    silinder: Optional[str]
    tahun: Optional[str]
    kodebbm: Optional[str]
    njop: Optional[Decimal]
    status: Optional[str]
    created_at: datetime
    created_by: Optional[str]
    updated_at: datetime
    updated_by: Optional[str]

    class Config:
        from_attributes = True
