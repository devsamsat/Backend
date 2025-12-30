from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class MasterFlowCreate(BaseModel):
    kdflow: str
    nmflow: str
    pkb: Optional[str] = None
    bbn1: Optional[str] = None
    bbn2: Optional[str] = None
    swd: Optional[str] = None
    atbkend: Optional[str] = None
    flowjr: Optional[str] = None
    stnkbaru: Optional[str] = None
    tnkb: Optional[str] = None
    sahstnk: Optional[str] = None
    perpanjangstnk: Optional[str] = None
    potongan: Optional[str] = None
    bataslayanan: Optional[int] = None
    satuan: Optional[str] = None
    status: Optional[str] = None
    created_by: Optional[str] = None
    updated_by: Optional[str] = None


class MasterFlowUpdate(BaseModel):
    nmflow: Optional[str] = None
    pkb: Optional[str] = None
    bbn1: Optional[str] = None
    bbn2: Optional[str] = None
    swd: Optional[str] = None
    atbkend: Optional[str] = None
    flowjr: Optional[str] = None
    stnkbaru: Optional[str] = None
    tnkb: Optional[str] = None
    sahstnk: Optional[str] = None
    perpanjangstnk: Optional[str] = None
    potongan: Optional[str] = None
    bataslayanan: Optional[int] = None
    satuan: Optional[str] = None
    status: Optional[str] = None
    updated_by: Optional[str] = None


class MasterFlowResponse(BaseModel):
    kdflow: str
    nmflow: str
    pkb: Optional[str]
    bbn1: Optional[str]
    bbn2: Optional[str]
    swd: Optional[str]
    atbkend: Optional[str]
    flowjr: Optional[str]
    stnkbaru: Optional[str]
    tnkb: Optional[str]
    sahstnk: Optional[str]
    perpanjangstnk: Optional[str]
    potongan: Optional[str]
    bataslayanan: Optional[int]
    satuan: Optional[str]
    status: Optional[str]
    created_at: datetime
    created_by: Optional[str]
    updated_at: datetime
    updated_by: Optional[str]

    class Config:
        from_attributes = True
