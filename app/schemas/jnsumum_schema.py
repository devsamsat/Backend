from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class JnsUmumCreate(BaseModel):
    kdumum: str
    nmumum: str
    keterangan: str
    status: Optional[str] = None
    created_by: Optional[str] = None
    updated_by: Optional[str] = None


class JnsUmumUpdate(BaseModel):
    nmumum: Optional[str] = None
    keterangan: Optional[str] = None
    status: Optional[str] = None
    updated_by: Optional[str] = None


class JnsUmumResponse(BaseModel):
    kdumum: str
    nmumum: str
    keterangan: str
    status: Optional[str]
    created_at: datetime
    created_by: Optional[str]
    updated_at: datetime
    updated_by: Optional[str]

    class Config:
        from_attributes = True
