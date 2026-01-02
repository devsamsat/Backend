from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel


class TransDataKohirCreate(BaseModel):
    penagih: str
    idwp: int
    masaawal: Optional[date] = None
    masaakhir: Optional[date] = None
    tglpenetapan: Optional[date] = None
    tglkurangbayar: Optional[date] = None
    keterangan: Optional[str] = None
    idupt: Optional[int] = None
    skrupt: Optional[str] = None
    validjr: Optional[str] = None
    validjrby: Optional[str] = None
    validpol: Optional[str] = None
    validpolby: Optional[str] = None
    ntpd: Optional[str] = None
    tglntpd: Optional[date] = None
    idbank: Optional[str] = None
    created_by: Optional[str] = None
    updated_by: Optional[str] = None


class TransDataKohirUpdate(BaseModel):
    penagih: Optional[str] = None
    idwp: Optional[int] = None
    masaawal: Optional[date] = None
    masaakhir: Optional[date] = None
    tglpenetapan: Optional[date] = None
    tglkurangbayar: Optional[date] = None
    keterangan: Optional[str] = None
    idupt: Optional[int] = None
    skrupt: Optional[str] = None
    validjr: Optional[str] = None
    validjrby: Optional[str] = None
    validpol: Optional[str] = None
    validpolby: Optional[str] = None
    ntpd: Optional[str] = None
    tglntpd: Optional[date] = None
    idbank: Optional[str] = None
    updated_by: Optional[str] = None


class TransDataKohirResponse(BaseModel):
    idkohir: int
    masaawal: Optional[date]
    masaakhir: Optional[date]
    tglpenetapan: Optional[date]
    penagih: str
    idwp: int
    tglkurangbayar: Optional[date]
    keterangan: Optional[str]
    idupt: Optional[int]
    skrupt: Optional[str]
    validjr: Optional[str]
    validjrby: Optional[str]
    validpol: Optional[str]
    validpolby: Optional[str]
    ntpd: Optional[str]
    tglntpd: Optional[date]
    idbank: Optional[str]
    created_at: datetime
    created_by: Optional[str]
    updated_at: datetime
    updated_by: Optional[str]

    class Config:
        from_attributes = True
