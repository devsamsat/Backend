from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class MasterKabKotaAllCreate(BaseModel):
    idprovinsi: int
    nmkabkota: str
    status: str
    kdkabkota: Optional[str] = None
    created_by: Optional[str] = None
    updated_by: Optional[str] = None


class MasterKabKotaAllUpdate(BaseModel):
    idprovinsi: Optional[int] = None
    nmkabkota: Optional[str] = None
    status: Optional[str] = None
    kdkabkota: Optional[str] = None
    updated_by: Optional[str] = None


class MasterKabKotaAllResponse(BaseModel):
    idkabkotaall: int
    idprovinsi: int
    nmkabkota: str
    status: str
    kdkabkota: Optional[str]
    created_at: datetime
    created_by: Optional[str]
    updated_at: datetime
    updated_by: Optional[str]

    class Config:
        from_attributes = True
