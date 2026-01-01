from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class MasterTeksCreate(BaseModel):
    datateks: str
    status: str
    created_by: Optional[str] = None
    updated_by: Optional[str] = None


class MasterTeksUpdate(BaseModel):
    datateks: Optional[str] = None
    status: Optional[str] = None
    updated_by: Optional[str] = None


class MasterTeksResponse(BaseModel):
    idteks: int
    datateks: str
    status: str
    created_at: datetime
    created_by: Optional[str]
    updated_at: datetime
    updated_by: Optional[str]

    class Config:
        from_attributes = True
