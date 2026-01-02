from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class MasterUunJopCreate(BaseModel):
    noperkada: Optional[str] = None
    isiperkada: Optional[str] = None
    tahun: Optional[str] = None
    status: Optional[str] = None
    keterangan: Optional[str] = None
    created_by: Optional[str] = None
    updated_by: Optional[str] = None


class MasterUunJopUpdate(BaseModel):
    noperkada: Optional[str] = None
    isiperkada: Optional[str] = None
    tahun: Optional[str] = None
    status: Optional[str] = None
    keterangan: Optional[str] = None
    updated_by: Optional[str] = None


class MasterUunJopResponse(BaseModel):
    iduunjop: int
    noperkada: Optional[str]
    isiperkada: Optional[str]
    tahun: Optional[str]
    status: Optional[str]
    keterangan: Optional[str]
    created_at: datetime
    created_by: Optional[str]
    updated_at: datetime
    updated_by: Optional[str]

    class Config:
        from_attributes = True
