from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class MasterPegawai:
    idpegawai: Optional[int]
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
    created_at: Optional[datetime] = None
    created_by: Optional[str] = None
    updated_at: Optional[datetime] = None
    updated_by: Optional[str] = None
