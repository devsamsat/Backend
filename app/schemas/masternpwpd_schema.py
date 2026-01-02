from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel


class MasterNpwpdCreate(BaseModel):
    statnpwpd: Optional[str] = None
    npwpd: str
    idbadan: Optional[int] = None
    idktp: Optional[int] = None
    tgldaftar: Optional[date] = None
    nib: Optional[str] = None
    namabadan: Optional[str] = None
    alamat: Optional[str] = None
    status: Optional[str] = None
    ket: Optional[str] = None
    created_by: Optional[str] = None
    updated_by: Optional[str] = None


class MasterNpwpdUpdate(BaseModel):
    statnpwpd: Optional[str] = None
    npwpd: Optional[str] = None
    idbadan: Optional[int] = None
    idktp: Optional[int] = None
    tgldaftar: Optional[date] = None
    nib: Optional[str] = None
    namabadan: Optional[str] = None
    alamat: Optional[str] = None
    status: Optional[str] = None
    ket: Optional[str] = None
    updated_by: Optional[str] = None


class MasterNpwpdResponse(BaseModel):
    idnpwpd: int
    statnpwpd: Optional[str]
    npwpd: str
    idbadan: Optional[int]
    idktp: Optional[int]
    tgldaftar: Optional[date]
    nib: Optional[str]
    namabadan: Optional[str]
    alamat: Optional[str]
    status: Optional[str]
    ket: Optional[str]
    created_at: datetime
    created_by: Optional[str]
    updated_at: datetime
    updated_by: Optional[str]

    class Config:
        from_attributes = True
