from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class AppGroupUserCreate(BaseModel):
    kdgroup: str
    nmgroup: str
    ket: Optional[str] = None
    created_by: Optional[str] = None
    updated_by: Optional[str] = None


class AppGroupUserUpdate(BaseModel):
    nmgroup: Optional[str] = None
    ket: Optional[str] = None
    created_by: Optional[str] = None
    updated_by: Optional[str] = None


class AppGroupUserResponse(BaseModel):
    kdgroup: str
    nmgroup: str
    ket: Optional[str]
    created_at: datetime
    created_by: Optional[str]
    updated_at: datetime
    updated_by: Optional[str]

    class Config:
        from_attributes = True
