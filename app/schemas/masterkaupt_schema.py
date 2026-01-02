from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class MasterKauptCreate(BaseModel):
    idupt: int
    idpegawai: Optional[int] = None
    created_by: Optional[str] = None
    updated_by: Optional[str] = None


class MasterKauptUpdate(BaseModel):
    idupt: Optional[int] = None
    idpegawai: Optional[int] = None
    updated_by: Optional[str] = None


class MasterKauptResponse(BaseModel):
    idkaupt: int
    idupt: int
    idpegawai: Optional[int]
    created_at: datetime
    created_by: Optional[str]
    updated_at: datetime
    updated_by: Optional[str]

    class Config:
        from_attributes = True
