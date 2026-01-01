from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class TransHistPendataanDetCreate(BaseModel):
    idhistpendataan: int
    idpenetapan: int
    nourut: int
    transid: str
    ket1: str
    usahaid: int
    tarifpajak: float
    histid: str
    status: str
    lokasi: Optional[str] = None
    created_by: Optional[str] = None
    updated_by: Optional[str] = None


class TransHistPendataanDetUpdate(BaseModel):
    idhistpendataan: Optional[int] = None
    idpenetapan: Optional[int] = None
    nourut: Optional[int] = None
    transid: Optional[str] = None
    ket1: Optional[str] = None
    usahaid: Optional[int] = None
    tarifpajak: Optional[float] = None
    histid: Optional[str] = None
    status: Optional[str] = None
    lokasi: Optional[str] = None
    updated_by: Optional[str] = None


class TransHistPendataanDetResponse(BaseModel):
    idhistpendataandet: int
    idhistpendataan: int
    idpenetapan: int
    nourut: int
    transid: str
    ket1: str
    usahaid: int
    tarifpajak: float
    histid: str
    status: str
    lokasi: Optional[str]
    created_at: datetime
    created_by: Optional[str]
    updated_at: datetime
    updated_by: Optional[str]

    class Config:
        from_attributes = True
