from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class TransWpDataFileCreate(BaseModel):
    idtwpdata: int
    namafile: Optional[str] = None
    direktory: Optional[str] = None
    extension: Optional[str] = None
    size: Optional[int] = None
    url: Optional[str] = None
    created_by: Optional[str] = None
    updated_by: Optional[str] = None


class TransWpDataFileUpdate(BaseModel):
    idtwpdata: Optional[int] = None
    namafile: Optional[str] = None
    direktory: Optional[str] = None
    extension: Optional[str] = None
    size: Optional[int] = None
    url: Optional[str] = None
    updated_by: Optional[str] = None


class TransWpDataFileResponse(BaseModel):
    idfile: int
    idtwpdata: int
    namafile: Optional[str]
    direktory: Optional[str]
    extension: Optional[str]
    size: Optional[int]
    url: Optional[str]
    created_at: datetime
    created_by: Optional[str]
    updated_at: datetime
    updated_by: Optional[str]

    class Config:
        from_attributes = True
