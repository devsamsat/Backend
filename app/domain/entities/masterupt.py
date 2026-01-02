from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class MasterUpt:
    idupt: Optional[int]
    kdupt: str
    nmupt: str
    upt_type: str
    idparent: Optional[int] = None
    kdlevel: Optional[str] = None
    akroupt: Optional[str] = None
    alamat: Optional[str] = None
    telepon: Optional[str] = None
    idbank: Optional[int] = None
    idkabkota: Optional[int] = None
    kepala: Optional[int] = None
    koordinator: Optional[int] = None
    bendahara: Optional[int] = None
    norekb: Optional[str] = None
    status: Optional[str] = None
    created_at: Optional[datetime] = None
    created_by: Optional[str] = None
    updated_at: Optional[datetime] = None
    updated_by: Optional[str] = None
