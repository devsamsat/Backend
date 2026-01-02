from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class MasterKelurahanCreate(BaseModel):
    idkecamatan: int
    nmkelurahan: str
    alamat: str
    telepon: str
    status: str
    kdkelurahan: Optional[str] = None
    kodepos: Optional[str] = None
    created_by: Optional[str] = None
    updated_by: Optional[str] = None


class MasterKelurahanUpdate(BaseModel):
    idkecamatan: Optional[int] = None
    nmkelurahan: Optional[str] = None
    alamat: Optional[str] = None
    telepon: Optional[str] = None
    status: Optional[str] = None
    kdkelurahan: Optional[str] = None
    kodepos: Optional[str] = None
    updated_by: Optional[str] = None


class MasterKelurahanResponse(BaseModel):
    idkelurahan: int
    idkecamatan: int
    nmkelurahan: str
    alamat: str
    telepon: str
    status: str
    kdkelurahan: Optional[str]
    kodepos: Optional[str]
    created_at: datetime
    created_by: Optional[str]
    updated_at: datetime
    updated_by: Optional[str]

    class Config:
        from_attributes = True
