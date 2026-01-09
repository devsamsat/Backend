from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class MasterKecamatanCreate(BaseModel):
    idkabkota: int
    nmkecamatan: str
    alamat: str
    telepon: str
    status: str
    kdkecamatan: Optional[str] = None
    fax: Optional[str] = None
    created_by: Optional[str] = None
    updated_by: Optional[str] = None


class MasterKecamatanUpdate(BaseModel):
    idkabkota: Optional[int] = None
    nmkecamatan: Optional[str] = None
    alamat: Optional[str] = None
    telepon: Optional[str] = None
    status: Optional[str] = None
    kdkecamatan: Optional[str] = None
    fax: Optional[str] = None
    updated_by: Optional[str] = None


class MasterKecamatanResponse(BaseModel):
    idkecamatan: int
    idkabkota: int
    nmkecamatan: str
    alamat: Optional[str]
    telepon: Optional[str]
    status: str
    kdkecamatan: Optional[str]
    fax: Optional[str]
    created_at: datetime
    created_by: Optional[str]
    updated_at: datetime
    updated_by: Optional[str]

    class Config:
        from_attributes = True
