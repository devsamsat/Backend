from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class MasterProvinsiCreate(BaseModel):
    kdprovinsi: str
    nmprovinsi: str
    status: str
    created_by: Optional[str] = None
    updated_by: Optional[str] = None


class MasterProvinsiUpdate(BaseModel):
    kdprovinsi: Optional[str] = None
    nmprovinsi: Optional[str] = None
    status: Optional[str] = None
    updated_by: Optional[str] = None


class MasterProvinsiResponse(BaseModel):
    idprovinsi: int
    kdprovinsi: str
    nmprovinsi: str
    status: str
    created_at: datetime
    created_by: Optional[str]
    updated_at: datetime
    updated_by: Optional[str]

    class Config:
        from_attributes = True
