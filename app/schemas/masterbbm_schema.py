from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class MasterBbmCreate(BaseModel):
    kodebbm: str
    namabbm: str
    keterangan: Optional[str] = None
    created_by: Optional[str] = None
    updated_by: Optional[str] = None


class MasterBbmUpdate(BaseModel):
    namabbm: Optional[str] = None
    keterangan: Optional[str] = None
    updated_by: Optional[str] = None


class MasterBbmResponse(BaseModel):
    kodebbm: str
    namabbm: str
    keterangan: Optional[str]
    created_at: datetime
    created_by: Optional[str]
    updated_at: datetime
    updated_by: Optional[str]

    class Config:
        from_attributes = True
