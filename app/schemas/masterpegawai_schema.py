from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class MasterPegawaiCreate(BaseModel):
    idktp: Optional[int] = None
    nip: str
    nik: Optional[str] = None
    nama: str
    idupt: int
    status: str
    jabatan: Optional[str] = None
    pangkat: Optional[str] = None
    golongan: Optional[str] = None
    uid: Optional[str] = None
    telepon: Optional[str] = None
    created_by: Optional[str] = None
    updated_by: Optional[str] = None


class MasterPegawaiUpdate(BaseModel):
    idktp: Optional[int] = None
    nip: Optional[str] = None
    nik: Optional[str] = None
    nama: Optional[str] = None
    idupt: Optional[int] = None
    status: Optional[str] = None
    jabatan: Optional[str] = None
    pangkat: Optional[str] = None
    golongan: Optional[str] = None
    uid: Optional[str] = None
    telepon: Optional[str] = None
    updated_by: Optional[str] = None


class MasterPegawaiResponse(BaseModel):
    idpegawai: int
    idktp: Optional[int]
    nip: str
    nik: Optional[str]
    nama: str
    idupt: int
    status: str
    jabatan: Optional[str]
    pangkat: Optional[str]
    golongan: Optional[str]
    uid: Optional[str]
    telepon: Optional[str]
    created_at: datetime
    created_by: Optional[str]
    updated_at: datetime
    updated_by: Optional[str]

    class Config:
        from_attributes = True
