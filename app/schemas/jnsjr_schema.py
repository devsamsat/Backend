from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class JnsJrCreate(BaseModel):
    jnsjrid: str
    kodejr: str
    goljns: str
    pu: str
    roda: int
    keterangan: Optional[str] = None
    created_by: Optional[str] = None
    updated_by: Optional[str] = None


class JnsJrUpdate(BaseModel):
    kodejr: Optional[str] = None
    goljns: Optional[str] = None
    pu: Optional[str] = None
    roda: Optional[int] = None
    keterangan: Optional[str] = None
    updated_by: Optional[str] = None


class JnsJrResponse(BaseModel):
    jnsjrid: str
    kodejr: str
    goljns: str
    pu: str
    roda: int
    keterangan: Optional[str]
    created_at: datetime
    created_by: Optional[str]
    updated_at: datetime
    updated_by: Optional[str]

    class Config:
        from_attributes = True
