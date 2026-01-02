from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class JnsProgresifCreate(BaseModel):
    kdprogresif: int
    progresifr2: float
    progresifr4: float
    created_by: Optional[str] = None
    updated_by: Optional[str] = None


class JnsProgresifUpdate(BaseModel):
    progresifr2: Optional[float] = None
    progresifr4: Optional[float] = None
    updated_by: Optional[str] = None


class JnsProgresifResponse(BaseModel):
    kdprogresif: int
    progresifr2: float
    progresifr4: float
    created_at: datetime
    created_by: Optional[str]
    updated_at: datetime
    updated_by: Optional[str]

    class Config:
        from_attributes = True
