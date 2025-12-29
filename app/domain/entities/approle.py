from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class AppRole:
    roleid: str
    idapp: Optional[int] = None
    role: Optional[str] = None
    role_type: Optional[str] = None
    menuid: Optional[str] = None
    parentid: Optional[str] = None
    bantuan: Optional[str] = None
    link: Optional[str] = None
    icon: Optional[str] = None
    kdlevel: Optional[int] = None
    is_show: Optional[int] = None
    created_at: Optional[datetime] = None
    created_by: Optional[str] = None
    updated_at: Optional[datetime] = None
    updated_by: Optional[str] = None
