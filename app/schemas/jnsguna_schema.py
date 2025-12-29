from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class JnsGunaCreate(BaseModel):
    kdguna: str
    guna: str
    gunaplat: Optional[str] = None
    progresif: Optional[float] = None
    groupbpkb: str
    created_by: Optional[str] = None
    updated_by: Optional[str] = None


class JnsGunaUpdate(BaseModel):
    guna: Optional[str] = None
    gunaplat: Optional[str] = None
    progresif: Optional[float] = None
    groupbpkb: Optional[str] = None
    updated_by: Optional[str] = None


class JnsGunaResponse(BaseModel):
    kdguna: str
    guna: str
    gunaplat: Optional[str]
    progresif: Optional[float]
    groupbpkb: Optional[str]
    created_at: datetime
    created_by: Optional[str]
    updated_at: datetime
    updated_by: Optional[str]

    class Config:
        from_attributes = True
