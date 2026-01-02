from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from typing import Optional


@dataclass
class MasterTarifNjop:
    idtarifnjop: Optional[int]
    iduunjop: int
    idrekd: Optional[int] = None
    kdjnstarif: Optional[str] = None
    namatarif: Optional[str] = None
    idmerk: Optional[int] = None
    tipe: Optional[str] = None
    silinder: Optional[str] = None
    tahun: Optional[str] = None
    kodebbm: Optional[str] = None
    njop: Optional[Decimal] = None
    status: Optional[str] = None
    created_at: Optional[datetime] = None
    created_by: Optional[str] = None
    updated_at: Optional[datetime] = None
    updated_by: Optional[str] = None
