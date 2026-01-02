from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class MasterRekdCreate(BaseModel):
    kdrek: str
    idparent: Optional[int] = None
    mtglevel: Optional[str] = None
    nmrek: Optional[str] = None
    kdjnspjk: Optional[str] = None
    rek_type: Optional[str] = None
    status: Optional[str] = None
    created_by: Optional[str] = None
    updated_by: Optional[str] = None


class MasterRekdUpdate(BaseModel):
    kdrek: Optional[str] = None
    idparent: Optional[int] = None
    mtglevel: Optional[str] = None
    nmrek: Optional[str] = None
    kdjnspjk: Optional[str] = None
    rek_type: Optional[str] = None
    status: Optional[str] = None
    updated_by: Optional[str] = None


class MasterRekdResponse(BaseModel):
    idrekd: int
    kdrek: str
    idparent: Optional[int]
    mtglevel: Optional[str]
    nmrek: Optional[str]
    kdjnspjk: Optional[str]
    rek_type: Optional[str]
    status: Optional[str]
    created_at: datetime
    created_by: Optional[str]
    updated_at: datetime
    updated_by: Optional[str]

    class Config:
        from_attributes = True
