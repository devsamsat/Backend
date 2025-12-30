from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class AppOtorCreate(BaseModel):
    kdgroup: str
    roleid: str
    ket: Optional[str] = None
    created_by: Optional[str] = None
    updated_by: Optional[str] = None


class AppOtorUpdate(BaseModel):
    ket: Optional[str] = None
    created_by: Optional[str] = None
    updated_by: Optional[str] = None


class AppOtorResponse(BaseModel):
    kdgroup: str
    roleid: str
    ket: Optional[str]
    created_at: datetime
    created_by: Optional[str]
    updated_at: datetime
    updated_by: Optional[str]

    class Config:
        from_attributes = True
