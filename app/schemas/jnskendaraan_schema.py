from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class JnsKendaraanCreate(BaseModel):
    jnskendid: str
    jnskend: str
    katid: str
    jnsjrid: Optional[str] = None
    golpjr: Optional[int] = None
    golujr: Optional[int] = None
    created_by: Optional[str] = None
    updated_by: Optional[str] = None


class JnsKendaraanUpdate(BaseModel):
    jnskend: Optional[str] = None
    katid: Optional[str] = None
    jnsjrid: Optional[str] = None
    golpjr: Optional[int] = None
    golujr: Optional[int] = None
    updated_by: Optional[str] = None


class JnsKendaraanResponse(BaseModel):
    jnskendid: str
    jnskend: str
    katid: str
    jnsjrid: Optional[str]
    golpjr: Optional[int]
    golujr: Optional[int]
    created_at: datetime
    created_by: Optional[str]
    updated_at: datetime
    updated_by: Optional[str]

    class Config:
        from_attributes = True
