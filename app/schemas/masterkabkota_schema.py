from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class MasterKabKotaCreate(BaseModel):
    idprovinsi: int
    nmkabkota: str
    akronim: str
    ibukota: str
    status: str
    bpkbid: str
    kdkabkota: Optional[str] = None
    created_by: Optional[str] = None
    updated_by: Optional[str] = None


class MasterKabKotaUpdate(BaseModel):
    idprovinsi: Optional[int] = None
    nmkabkota: Optional[str] = None
    akronim: Optional[str] = None
    ibukota: Optional[str] = None
    status: Optional[str] = None
    bpkbid: Optional[str] = None
    kdkabkota: Optional[str] = None
    updated_by: Optional[str] = None


class MasterKabKotaResponse(BaseModel):
    idkabkota: int
    idprovinsi: int
    nmkabkota: str
    akronim: Optional[str]
    ibukota: Optional[str]
    status: str
    bpkbid: Optional[str]
    kdkabkota: Optional[str]
    created_at: datetime
    created_by: Optional[str]
    updated_at: datetime
    updated_by: Optional[str]

    class Config:
        from_attributes = True
