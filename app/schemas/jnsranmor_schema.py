from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class JnsRanmorCreate(BaseModel):
    kdranmor: str
    nmranmor: str
    snid: str
    status: Optional[str] = None
    created_by: Optional[str] = None
    updated_by: Optional[str] = None


class JnsRanmorUpdate(BaseModel):
    nmranmor: Optional[str] = None
    snid: Optional[str] = None
    status: Optional[str] = None
    updated_by: Optional[str] = None


class JnsRanmorResponse(BaseModel):
    kdranmor: str
    nmranmor: str
    snid: str
    status: Optional[str]
    created_at: datetime
    created_by: Optional[str]
    updated_at: datetime
    updated_by: Optional[str]

    class Config:
        from_attributes = True
