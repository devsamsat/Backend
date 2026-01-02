from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class JnsPlatCreate(BaseModel):
    kdplat: str
    plat: str
    pu: str
    platjr: int
    numpkb: float
    numbbn1: float
    numbbn2: float
    umorg: float
    umbrg: float
    dnumpkb: float
    dnumbbn: float
    dumorg: float
    dumbrg: float
    abpkb: float
    abbbn1: float
    abbbn2: float
    numfiskal: float
    snid: str
    opspkb: float
    opsbbn: float
    opsnumpkb: float
    opsnumbbn1: float
    opsnumbbn2: float
    opsdnumpkb: float
    opsdnumbbn: float
    minnumpkb: float
    minnumbbn1: float
    minnumbbn2: float
    created_by: Optional[str] = None
    updated_by: Optional[str] = None


class JnsPlatUpdate(BaseModel):
    plat: Optional[str] = None
    pu: Optional[str] = None
    platjr: Optional[int] = None
    numpkb: Optional[float] = None
    numbbn1: Optional[float] = None
    numbbn2: Optional[float] = None
    umorg: Optional[float] = None
    umbrg: Optional[float] = None
    dnumpkb: Optional[float] = None
    dnumbbn: Optional[float] = None
    dumorg: Optional[float] = None
    dumbrg: Optional[float] = None
    abpkb: Optional[float] = None
    abbbn1: Optional[float] = None
    abbbn2: Optional[float] = None
    numfiskal: Optional[float] = None
    snid: Optional[str] = None
    opspkb: Optional[float] = None
    opsbbn: Optional[float] = None
    opsnumpkb: Optional[float] = None
    opsnumbbn1: Optional[float] = None
    opsnumbbn2: Optional[float] = None
    opsdnumpkb: Optional[float] = None
    opsdnumbbn: Optional[float] = None
    minnumpkb: Optional[float] = None
    minnumbbn1: Optional[float] = None
    minnumbbn2: Optional[float] = None
    updated_by: Optional[str] = None


class JnsPlatResponse(BaseModel):
    kdplat: str
    plat: str
    pu: str
    platjr: int
    numpkb: float
    numbbn1: float
    numbbn2: float
    umorg: float
    umbrg: float
    dnumpkb: float
    dnumbbn: float
    dumorg: float
    dumbrg: float
    abpkb: float
    abbbn1: float
    abbbn2: float
    numfiskal: float
    snid: str
    opspkb: float
    opsbbn: float
    opsnumpkb: float
    opsnumbbn1: float
    opsnumbbn2: float
    opsdnumpkb: float
    opsdnumbbn: float
    minnumpkb: float
    minnumbbn1: float
    minnumbbn2: float
    created_at: datetime
    created_by: Optional[str]
    updated_at: datetime
    updated_by: Optional[str]

    class Config:
        from_attributes = True
