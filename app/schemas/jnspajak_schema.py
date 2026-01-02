from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class JnsPajakCreate(BaseModel):
    kdjnspjk: str
    nmjnspjk: str
    keterangan: Optional[str] = None
    created_by: Optional[str] = None
    updated_by: Optional[str] = None


class JnsPajakUpdate(BaseModel):
    nmjnspjk: Optional[str] = None
    keterangan: Optional[str] = None
    updated_by: Optional[str] = None


class JnsPajakResponse(BaseModel):
    kdjnspjk: str
    nmjnspjk: str
    keterangan: Optional[str]
    created_at: datetime
    created_by: Optional[str]
    updated_at: datetime
    updated_by: Optional[str]

    class Config:
        from_attributes = True
