from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class AppUser:
    userid: str
    kdtahap: str
    kdgroup: str
    idupt: Optional[int] = None
    pwd: Optional[str] = None
    idpeg: Optional[int] = None
    nik: Optional[str] = None
    nama: Optional[str] = None
    email: Optional[str] = None
    created_at: Optional[datetime] = None
    created_by: Optional[str] = None
    updated_at: Optional[datetime] = None
    updated_by: Optional[str] = None
