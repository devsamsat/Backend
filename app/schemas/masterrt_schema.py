from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class MasterRtCreate(BaseModel):
    idrw: int
    status: str
    kdrt: Optional[str] = None
    created_by: Optional[str] = None
    updated_by: Optional[str] = None


class MasterRtUpdate(BaseModel):
    idrw: Optional[int] = None
    status: Optional[str] = None
    kdrt: Optional[str] = None
    updated_by: Optional[str] = None


class MasterRtResponse(BaseModel):
    idrt: int
    idrw: int
    status: str
    kdrt: Optional[str]
    created_at: datetime
    created_by: Optional[str]
    updated_at: datetime
    updated_by: Optional[str]

    class Config:
        from_attributes = True
