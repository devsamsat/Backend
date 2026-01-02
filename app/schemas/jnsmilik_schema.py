from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class JnsMilikCreate(BaseModel):
    kdmilik: str
    milik: str
    bpkpid: str
    status: Optional[str] = None
    created_by: Optional[str] = None
    updated_by: Optional[str] = None


class JnsMilikUpdate(BaseModel):
    milik: Optional[str] = None
    bpkpid: Optional[str] = None
    status: Optional[str] = None
    updated_by: Optional[str] = None


class JnsMilikResponse(BaseModel):
    kdmilik: str
    milik: str
    bpkpid: str
    status: Optional[str]
    created_at: datetime
    created_by: Optional[str]
    updated_at: datetime
    updated_by: Optional[str]

    class Config:
        from_attributes = True
