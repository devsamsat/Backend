from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class MasterAbDetCreate(BaseModel):
    idab: int
    idjnsd: int
    created_by: Optional[str] = None
    updated_by: Optional[str] = None


class MasterAbDetUpdate(BaseModel):
    idab: Optional[int] = None
    idjnsd: Optional[int] = None
    updated_by: Optional[str] = None


class MasterAbDetResponse(BaseModel):
    idabdet: int
    idab: int
    idjnsd: int
    created_at: datetime
    created_by: Optional[str]
    updated_at: datetime
    updated_by: Optional[str]

    class Config:
        from_attributes = True
