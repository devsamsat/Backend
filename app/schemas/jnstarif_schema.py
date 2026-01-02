from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class JnsTarifCreate(BaseModel):
    kdjnstarif: str
    nmjnstarif: str
    idupt: int
    jnskendid: Optional[str] = None
    idrekd: Optional[int] = None
    status: Optional[str] = None
    created_by: Optional[str] = None
    updated_by: Optional[str] = None


class JnsTarifUpdate(BaseModel):
    nmjnstarif: Optional[str] = None
    idupt: Optional[int] = None
    jnskendid: Optional[str] = None
    idrekd: Optional[int] = None
    status: Optional[str] = None
    updated_by: Optional[str] = None


class JnsTarifResponse(BaseModel):
    kdjnstarif: str
    nmjnstarif: str
    idupt: int
    jnskendid: Optional[str]
    idrekd: Optional[int]
    status: Optional[str]
    created_at: datetime
    created_by: Optional[str]
    updated_at: datetime
    updated_by: Optional[str]

    class Config:
        from_attributes = True
