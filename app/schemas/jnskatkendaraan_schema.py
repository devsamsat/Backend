from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class JnsKatKendaraanCreate(BaseModel):
    katid: str
    kendaraan: str
    jenisbpkb: str
    status: Optional[str] = None
    created_by: Optional[str] = None
    updated_by: Optional[str] = None


class JnsKatKendaraanUpdate(BaseModel):
    kendaraan: Optional[str] = None
    jenisbpkb: Optional[str] = None
    status: Optional[str] = None
    updated_by: Optional[str] = None


class JnsKatKendaraanResponse(BaseModel):
    katid: str
    kendaraan: str
    jenisbpkb: str
    status: Optional[str]
    created_at: datetime
    created_by: Optional[str]
    updated_at: datetime
    updated_by: Optional[str]

    class Config:
        from_attributes = True
