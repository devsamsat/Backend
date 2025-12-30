from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class MasterBendaharaCreate(BaseModel):
    idpegawai: int
    idbank: int
    norek: str
    namarek: str
    jnsbend: str
    status: str
    jabatan: Optional[str] = None
    pangkat: Optional[str] = None
    uid: Optional[str] = None
    koordinator: Optional[int] = None
    idreknrc: Optional[int] = None
    telepon: Optional[str] = None
    ket: Optional[str] = None
    created_by: Optional[str] = None
    updated_by: Optional[str] = None


class MasterBendaharaUpdate(BaseModel):
    idpegawai: Optional[int] = None
    idbank: Optional[int] = None
    norek: Optional[str] = None
    namarek: Optional[str] = None
    jnsbend: Optional[str] = None
    status: Optional[str] = None
    jabatan: Optional[str] = None
    pangkat: Optional[str] = None
    uid: Optional[str] = None
    koordinator: Optional[int] = None
    idreknrc: Optional[int] = None
    telepon: Optional[str] = None
    ket: Optional[str] = None
    updated_by: Optional[str] = None


class MasterBendaharaResponse(BaseModel):
    idbend: int
    idpegawai: int
    idbank: int
    norek: str
    namarek: str
    jnsbend: str
    status: str
    jabatan: Optional[str]
    pangkat: Optional[str]
    uid: Optional[str]
    koordinator: Optional[int]
    idreknrc: Optional[int]
    telepon: Optional[str]
    ket: Optional[str]
    created_at: datetime
    created_by: Optional[str]
    updated_at: datetime
    updated_by: Optional[str]

    class Config:
        from_attributes = True
