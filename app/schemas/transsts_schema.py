from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel


class TransStsCreate(BaseModel):
    idupt: int
    idbend: int
    nosts: str
    keterangan: str
    statbayar: str
    setorandari: Optional[str] = None
    tglsts: Optional[date] = None
    ntpd: Optional[str] = None
    tglntpd: Optional[date] = None
    statsts: Optional[int] = None
    created_by: Optional[str] = None
    updated_by: Optional[str] = None


class TransStsUpdate(BaseModel):
    idupt: Optional[int] = None
    idbend: Optional[int] = None
    nosts: Optional[str] = None
    keterangan: Optional[str] = None
    statbayar: Optional[str] = None
    setorandari: Optional[str] = None
    tglsts: Optional[date] = None
    ntpd: Optional[str] = None
    tglntpd: Optional[date] = None
    statsts: Optional[int] = None
    updated_by: Optional[str] = None


class TransStsResponse(BaseModel):
    idsts: int
    idupt: int
    idbend: int
    nosts: str
    keterangan: str
    statbayar: str
    setorandari: Optional[str]
    tglsts: Optional[date]
    ntpd: Optional[str]
    tglntpd: Optional[date]
    statsts: Optional[int]
    created_at: datetime
    created_by: Optional[str]
    updated_at: datetime
    updated_by: Optional[str]

    class Config:
        from_attributes = True
