from datetime import datetime
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel


class TransStsDetCreate(BaseModel):
    idsts: int
    idrekd: int
    nilaists: Decimal
    jenis: str
    created_by: Optional[str] = None
    updated_by: Optional[str] = None


class TransStsDetUpdate(BaseModel):
    idsts: Optional[int] = None
    idrekd: Optional[int] = None
    nilaists: Optional[Decimal] = None
    jenis: Optional[str] = None
    updated_by: Optional[str] = None


class TransStsDetResponse(BaseModel):
    idstsdet: int
    idsts: int
    idrekd: int
    nilaists: Decimal
    jenis: str
    created_at: datetime
    created_by: Optional[str]
    updated_at: datetime
    updated_by: Optional[str]

    class Config:
        from_attributes = True
