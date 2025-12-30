from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class AppUser:
    userid: str
    idupt: Optional[int]
    kdtahap: str
    pwd: Optional[str]
    idpeg: Optional[int]
    kdgroup: str
    nik: Optional[str]
    nama: Optional[str]
    email: Optional[str]
    created_at: Optional[datetime] = None
    created_by: Optional[str] = None
    updated_at: Optional[datetime] = None
    updated_by: Optional[str] = None
