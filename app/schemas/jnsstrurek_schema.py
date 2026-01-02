from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class JnsStruRekCreate(BaseModel):
    mtglevel: str
    nmlevel: str
    keterangan: str
    created_by: Optional[str] = None
    updated_by: Optional[str] = None


class JnsStruRekUpdate(BaseModel):
    nmlevel: Optional[str] = None
    keterangan: Optional[str] = None
    updated_by: Optional[str] = None


class JnsStruRekResponse(BaseModel):
    mtglevel: str
    nmlevel: str
    keterangan: str
    created_at: datetime
    created_by: Optional[str]
    updated_at: datetime
    updated_by: Optional[str]

    class Config:
        from_attributes = True
