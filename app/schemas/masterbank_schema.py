from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class MasterBankCreate(BaseModel):
    kodebank: str
    namabank: str
    akronimbank: Optional[str] = None
    cabangbank: Optional[str] = None
    alamatbank: Optional[str] = None
    status: Optional[str] = None
    created_by: Optional[str] = None
    updated_by: Optional[str] = None


class MasterBankUpdate(BaseModel):
    kodebank: Optional[str] = None
    namabank: Optional[str] = None
    akronimbank: Optional[str] = None
    cabangbank: Optional[str] = None
    alamatbank: Optional[str] = None
    status: Optional[str] = None
    updated_by: Optional[str] = None


class MasterBankResponse(BaseModel):
    idbank: int
    kodebank: str
    namabank: str
    akronimbank: Optional[str]
    cabangbank: Optional[str]
    alamatbank: Optional[str]
    status: Optional[str]
    created_at: datetime
    created_by: Optional[str]
    updated_at: datetime
    updated_by: Optional[str]

    class Config:
        from_attributes = True
