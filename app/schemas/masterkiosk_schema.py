from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class MasterKioskCreate(BaseModel):
    kodekiosk: str
    datakiosk: str
    level: str
    status: str
    idparent: Optional[int] = None
    created_by: Optional[str] = None
    updated_by: Optional[str] = None


class MasterKioskUpdate(BaseModel):
    kodekiosk: Optional[str] = None
    datakiosk: Optional[str] = None
    level: Optional[str] = None
    status: Optional[str] = None
    idparent: Optional[int] = None
    updated_by: Optional[str] = None


class MasterKioskResponse(BaseModel):
    idkios: int
    kodekiosk: str
    datakiosk: str
    level: str
    status: str
    idparent: Optional[int]
    created_at: datetime
    created_by: Optional[str]
    updated_at: datetime
    updated_by: Optional[str]

    class Config:
        from_attributes = True
