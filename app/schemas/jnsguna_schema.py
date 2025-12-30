from datetime import datetime
from decimal import Decimal
from typing import Optional
from pydantic import BaseModel


class JnsGunaCreate(BaseModel):
    kdguna: str
    guna: str
    gunaplat: Optional[str] = None
    progresif: Optional[Decimal] = None
    groupbpkb: str
    created_by: Optional[str] = None
    updated_by: Optional[str] = None


class JnsGunaUpdate(BaseModel):
    guna: Optional[str] = None
    gunaplat: Optional[str] = None
    progresif: Optional[Decimal] = None
    groupbpkb: Optional[str] = None
    created_by: Optional[str] = None
    updated_by: Optional[str] = None


class JnsGunaResponse(BaseModel):
    kdguna: str
    guna: str
    gunaplat: Optional[str]
    progresif: Optional[Decimal]
    groupbpkb: str
    created_at: datetime
    created_by: Optional[str]
    updated_at: datetime
    updated_by: Optional[str]

    class Config:
        from_attributes = True
