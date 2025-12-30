from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel


class MasterBadanCreate(BaseModel):
    namabadan: str
    nohp: str
    alamat: str
    nib: Optional[str] = None
    idktp: Optional[int] = None
    tgldaftar: Optional[date] = None
    idprovinsi: Optional[int] = None
    idkabkokta: Optional[int] = None
    ket: Optional[str] = None
    created_by: Optional[str] = None
    updated_by: Optional[str] = None


class MasterBadanUpdate(BaseModel):
    namabadan: Optional[str] = None
    nohp: Optional[str] = None
    alamat: Optional[str] = None
    nib: Optional[str] = None
    idktp: Optional[int] = None
    tgldaftar: Optional[date] = None
    idprovinsi: Optional[int] = None
    idkabkokta: Optional[int] = None
    ket: Optional[str] = None
    updated_by: Optional[str] = None


class MasterBadanResponse(BaseModel):
    idbadan: int
    namabadan: str
    nohp: str
    alamat: str
    nib: Optional[str]
    idktp: Optional[int]
    tgldaftar: Optional[date]
    idprovinsi: Optional[int]
    idkabkokta: Optional[int]
    ket: Optional[str]
    created_at: datetime
    created_by: Optional[str]
    updated_at: datetime
    updated_by: Optional[str]

    class Config:
        from_attributes = True
