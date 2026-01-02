from datetime import datetime
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel


class TransPendataanDetCreate(BaseModel):
    idpendataan: int
    idpenetapan: int
    nourut: int
    transid: str
    ket1: str
    usahaid: int
    tarifpajak: Decimal
    status: str
    lokasi: Optional[str] = None
    created_by: Optional[str] = None
    updated_by: Optional[str] = None


class TransPendataanDetUpdate(BaseModel):
    idpendataan: Optional[int] = None
    idpenetapan: Optional[int] = None
    nourut: Optional[int] = None
    transid: Optional[str] = None
    ket1: Optional[str] = None
    usahaid: Optional[int] = None
    tarifpajak: Optional[Decimal] = None
    status: Optional[str] = None
    lokasi: Optional[str] = None
    updated_by: Optional[str] = None


class TransPendataanDetResponse(BaseModel):
    idpendataandet: int
    idpendataan: int
    idpenetapan: int
    nourut: int
    transid: str
    ket1: str
    usahaid: int
    tarifpajak: Decimal
    status: str
    lokasi: Optional[str]
    created_at: datetime
    created_by: Optional[str]
    updated_at: datetime
    updated_by: Optional[str]

    class Config:
        from_attributes = True
