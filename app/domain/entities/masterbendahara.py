from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class MasterBendahara:
    idbend: Optional[int]
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
    created_at: Optional[datetime] = None
    created_by: Optional[str] = None
    updated_at: Optional[datetime] = None
    updated_by: Optional[str] = None
