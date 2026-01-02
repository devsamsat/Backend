from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class MasterRekNrcCreate(BaseModel):
    kdrek: str
    mtglevel: Optional[str] = None
    nmrek: Optional[str] = None
    rek_type: Optional[str] = None
    created_by: Optional[str] = None
    updated_by: Optional[str] = None


class MasterRekNrcUpdate(BaseModel):
    kdrek: Optional[str] = None
    mtglevel: Optional[str] = None
    nmrek: Optional[str] = None
    rek_type: Optional[str] = None
    updated_by: Optional[str] = None


class MasterRekNrcResponse(BaseModel):
    idreknrc: int
    kdrek: str
    mtglevel: Optional[str]
    nmrek: Optional[str]
    rek_type: Optional[str]
    created_at: datetime
    created_by: Optional[str]
    updated_at: datetime
    updated_by: Optional[str]

    class Config:
        from_attributes = True
