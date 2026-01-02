from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class MasterJnsPendapatanCreate(BaseModel):
    nmjnspendapatan: str
    parentid: Optional[int] = None
    kdrek: Optional[str] = None
    jatuhtempo: Optional[int] = None
    status: Optional[str] = None
    selfassessment: Optional[str] = None
    katid: Optional[str] = None
    created_by: Optional[str] = None
    updated_by: Optional[str] = None


class MasterJnsPendapatanUpdate(BaseModel):
    nmjnspendapatan: Optional[str] = None
    parentid: Optional[int] = None
    kdrek: Optional[str] = None
    jatuhtempo: Optional[int] = None
    status: Optional[str] = None
    selfassessment: Optional[str] = None
    katid: Optional[str] = None
    updated_by: Optional[str] = None


class MasterJnsPendapatanResponse(BaseModel):
    idjnsd: int
    nmjnspendapatan: str
    parentid: Optional[int]
    kdrek: Optional[str]
    jatuhtempo: Optional[int]
    status: Optional[str]
    selfassessment: Optional[str]
    katid: Optional[str]
    created_at: datetime
    created_by: Optional[str]
    updated_at: datetime
    updated_by: Optional[str]

    class Config:
        from_attributes = True
