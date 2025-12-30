from dataclasses import dataclass
from datetime import date, datetime
from typing import Optional


@dataclass
class MasterBadan:
    idbadan: Optional[int]
    namabadan: str
    nohp: str
    alamat: str
    nib: Optional[str] = None
    idktp: Optional[int] = None
    tgldaftar: Optional[date] = None
    idprovinsi: Optional[int] = None
    idkabkokta: Optional[int] = None
    ket: Optional[str] = None
    created_at: Optional[datetime] = None
    created_by: Optional[str] = None
    updated_at: Optional[datetime] = None
    updated_by: Optional[str] = None
