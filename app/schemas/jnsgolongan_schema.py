from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class JnsGolonganCreate(BaseModel):
    jnsgolid: str
    golongan: str
    katid: Optional[str] = None
    jnskendid: Optional[str] = None
    viewall: Optional[str] = None
    status: Optional[str] = None
    created_by: Optional[str] = None
    updated_by: Optional[str] = None


class JnsGolonganUpdate(BaseModel):
    golongan: Optional[str] = None
    katid: Optional[str] = None
    jnskendid: Optional[str] = None
    viewall: Optional[str] = None
    status: Optional[str] = None
    created_by: Optional[str] = None
    updated_by: Optional[str] = None


class JnsGolonganResponse(BaseModel):
    jnsgolid: str
    golongan: str
    katid: Optional[str]
    jnskendid: Optional[str]
    viewall: Optional[str]
    status: Optional[str]
    created_at: datetime
    created_by: Optional[str]
    updated_at: datetime
    updated_by: Optional[str]

    class Config:
        from_attributes = True
