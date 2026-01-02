from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class TransWpDataAntriCreate(BaseModel):
    idtwpdata: int
    noantri: str
    idktp: Optional[int] = None
    statantri: Optional[str] = None
    ket: Optional[str] = None
    tglantri: Optional[str] = None
    created_by: Optional[str] = None
    updated_by: Optional[str] = None


class TransWpDataAntriUpdate(BaseModel):
    idtwpdata: Optional[int] = None
    noantri: Optional[str] = None
    idktp: Optional[int] = None
    statantri: Optional[str] = None
    ket: Optional[str] = None
    tglantri: Optional[str] = None
    updated_by: Optional[str] = None


class TransWpDataAntriResponse(BaseModel):
    idantri: int
    idtwpdata: int
    noantri: str
    idktp: Optional[int]
    statantri: Optional[str]
    ket: Optional[str]
    tglantri: Optional[str]
    created_at: datetime
    created_by: Optional[str]
    updated_at: datetime
    updated_by: Optional[str]

    class Config:
        from_attributes = True
