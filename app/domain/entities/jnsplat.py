from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class JnsPlat:
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
    created_at: Optional[datetime] = None
    created_by: Optional[str] = None
    updated_at: Optional[datetime] = None
    updated_by: Optional[str] = None
