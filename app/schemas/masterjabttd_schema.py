from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class MasterJabTtdCreate(BaseModel):
    idpegawai: int
    kddok: str
    jabatan: Optional[str] = None
    ket: Optional[str] = None
    status: Optional[str] = None
    created_by: Optional[str] = None
    updated_by: Optional[str] = None


class MasterJabTtdUpdate(BaseModel):
    idpegawai: Optional[int] = None
    kddok: Optional[str] = None
    jabatan: Optional[str] = None
    ket: Optional[str] = None
    status: Optional[str] = None
    updated_by: Optional[str] = None


class MasterJabTtdResponse(BaseModel):
    idjabttd: int
    idpegawai: int
    kddok: str
    jabatan: Optional[str]
    ket: Optional[str]
    status: Optional[str]
    created_at: datetime
    created_by: Optional[str]
    updated_at: datetime
    updated_by: Optional[str]

    class Config:
        from_attributes = True
