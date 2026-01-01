from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel


class MasterWpDataCreate(BaseModel):
    idjnsd: int
    idwp: int
    tglpendataan: Optional[date] = None
    created_by: Optional[str] = None
    updated_by: Optional[str] = None


class MasterWpDataUpdate(BaseModel):
    idjnsd: Optional[int] = None
    idwp: Optional[int] = None
    tglpendataan: Optional[date] = None
    updated_by: Optional[str] = None


class MasterWpDataResponse(BaseModel):
    idwpdata: int
    idjnsd: int
    idwp: int
    tglpendataan: Optional[date]
    created_at: datetime
    created_by: Optional[str]
    updated_at: datetime
    updated_by: Optional[str]

    class Config:
        from_attributes = True
