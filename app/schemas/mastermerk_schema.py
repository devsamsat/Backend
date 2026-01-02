from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class MasterMerkCreate(BaseModel):
    kdmerk: Optional[str] = None
    nmmerk: str
    keterangan: Optional[str] = None
    status: Optional[str] = None
    created_by: Optional[str] = None
    updated_by: Optional[str] = None


class MasterMerkUpdate(BaseModel):
    kdmerk: Optional[str] = None
    nmmerk: Optional[str] = None
    keterangan: Optional[str] = None
    status: Optional[str] = None
    updated_by: Optional[str] = None


class MasterMerkResponse(BaseModel):
    idmerk: int
    kdmerk: Optional[str]
    nmmerk: str
    keterangan: Optional[str]
    status: Optional[str]
    created_at: datetime
    created_by: Optional[str]
    updated_at: datetime
    updated_by: Optional[str]

    class Config:
        from_attributes = True
