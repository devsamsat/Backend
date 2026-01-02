from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from typing import Optional


@dataclass
class MasterTarif:
    idtarif: Optional[int]
    kdjnspjk: str
    jnskendid: Optional[str] = None
    satuan: Optional[str] = None
    awal: Optional[Decimal] = None
    akhir: Optional[Decimal] = None
    keterangan: Optional[str] = None
    kdflow: Optional[str] = None
    kdplat: Optional[str] = None
    statumum: Optional[str] = None
    tarif: Optional[Decimal] = None
    created_at: Optional[datetime] = None
    created_by: Optional[str] = None
    updated_at: Optional[datetime] = None
    updated_by: Optional[str] = None
