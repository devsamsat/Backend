from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel


class TransWpDataCreate(BaseModel):
    idnpwpd: int
    kdflow: Optional[str] = None
    tgldaftar: Optional[date] = None
    created_by: Optional[str] = None
    updated_by: Optional[str] = None


class TransWpDataUpdate(BaseModel):
    idnpwpd: Optional[int] = None
    kdflow: Optional[str] = None
    tgldaftar: Optional[date] = None
    updated_by: Optional[str] = None


class TransWpDataResponse(BaseModel):
    idtwpdata: int
    idnpwpd: int
    kdflow: Optional[str]
    tgldaftar: Optional[date]
    created_at: datetime
    created_by: Optional[str]
    updated_at: datetime
    updated_by: Optional[str]

    class Config:
        from_attributes = True
