from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class JnsHistCreate(BaseModel):
    kdhist: str
    nmhist: str
    kdflow: Optional[str] = None
    status: Optional[str] = None
    created_by: Optional[str] = None
    updated_by: Optional[str] = None


class JnsHistUpdate(BaseModel):
    nmhist: Optional[str] = None
    kdflow: Optional[str] = None
    status: Optional[str] = None
    updated_by: Optional[str] = None


class JnsHistResponse(BaseModel):
    kdhist: str
    nmhist: str
    kdflow: Optional[str]
    status: Optional[str]
    created_at: datetime
    created_by: Optional[str]
    updated_at: datetime
    updated_by: Optional[str]

    class Config:
        from_attributes = True
