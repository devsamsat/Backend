from dataclasses import dataclass
from datetime import date, datetime
from typing import Optional


@dataclass
class MasterNpwpd:
    idnpwpd: Optional[int]
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
    created_at: Optional[datetime] = None
    created_by: Optional[str] = None
    updated_at: Optional[datetime] = None
    updated_by: Optional[str] = None
