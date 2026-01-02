from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class MasterKbDetCreate(BaseModel):
    idkb: int
    idjnsd: int
    created_by: Optional[str] = None
    updated_by: Optional[str] = None


class MasterKbDetUpdate(BaseModel):
    idkb: Optional[int] = None
    idjnsd: Optional[int] = None
    updated_by: Optional[str] = None


class MasterKbDetResponse(BaseModel):
    idkbdet: int
    idkb: int
    idjnsd: int
    created_at: datetime
    created_by: Optional[str]
    updated_at: datetime
    updated_by: Optional[str]

    class Config:
        from_attributes = True
