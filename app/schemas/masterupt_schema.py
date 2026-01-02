from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class MasterUptCreate(BaseModel):
    kdupt: str
    nmupt: str
    upt_type: str
    idparent: Optional[int] = None
    kdlevel: Optional[str] = None
    akroupt: Optional[str] = None
    alamat: Optional[str] = None
    telepon: Optional[str] = None
    idbank: Optional[int] = None
    idkabkota: Optional[int] = None
    kepala: Optional[int] = None
    koordinator: Optional[int] = None
    bendahara: Optional[int] = None
    norekb: Optional[str] = None
    status: Optional[str] = None
    created_by: Optional[str] = None
    updated_by: Optional[str] = None


class MasterUptUpdate(BaseModel):
    kdupt: Optional[str] = None
    nmupt: Optional[str] = None
    upt_type: Optional[str] = None
    idparent: Optional[int] = None
    kdlevel: Optional[str] = None
    akroupt: Optional[str] = None
    alamat: Optional[str] = None
    telepon: Optional[str] = None
    idbank: Optional[int] = None
    idkabkota: Optional[int] = None
    kepala: Optional[int] = None
    koordinator: Optional[int] = None
    bendahara: Optional[int] = None
    norekb: Optional[str] = None
    status: Optional[str] = None
    updated_by: Optional[str] = None


class MasterUptResponse(BaseModel):
    idupt: int
    idparent: Optional[int]
    kdupt: str
    nmupt: str
    kdlevel: Optional[str]
    upt_type: str
    akroupt: Optional[str]
    alamat: Optional[str]
    telepon: Optional[str]
    idbank: Optional[int]
    idkabkota: Optional[int]
    kepala: Optional[int]
    koordinator: Optional[int]
    bendahara: Optional[int]
    norekb: Optional[str]
    status: Optional[str]
    created_at: datetime
    created_by: Optional[str]
    updated_at: datetime
    updated_by: Optional[str]

    class Config:
        from_attributes = True
