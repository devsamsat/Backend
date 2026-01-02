from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class MasterRwCreate(BaseModel):
    idkelurahan: int
    alamat: str
    status: str
    kdrw: Optional[str] = None
    created_by: Optional[str] = None
    updated_by: Optional[str] = None


class MasterRwUpdate(BaseModel):
    idkelurahan: Optional[int] = None
    alamat: Optional[str] = None
    status: Optional[str] = None
    kdrw: Optional[str] = None
    updated_by: Optional[str] = None


class MasterRwResponse(BaseModel):
    idrw: int
    idkelurahan: int
    alamat: str
    status: str
    kdrw: Optional[str]
    created_at: datetime
    created_by: Optional[str]
    updated_at: datetime
    updated_by: Optional[str]

    class Config:
        from_attributes = True
