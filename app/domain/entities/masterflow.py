from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class MasterFlow:
    kdflow: str
    nmflow: str
    pkb: Optional[str] = None
    bbn1: Optional[str] = None
    bbn2: Optional[str] = None
    swd: Optional[str] = None
    atbkend: Optional[str] = None
    flowjr: Optional[str] = None
    stnkbaru: Optional[str] = None
    tnkb: Optional[str] = None
    sahstnk: Optional[str] = None
    perpanjangstnk: Optional[str] = None
    potongan: Optional[str] = None
    bataslayanan: Optional[int] = None
    satuan: Optional[str] = None
    status: Optional[str] = None
    created_at: Optional[datetime] = None
    created_by: Optional[str] = None
    updated_at: Optional[datetime] = None
    updated_by: Optional[str] = None
