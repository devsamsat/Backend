from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class AppRole:
    roleid: str
    idapp: Optional[int]
    role: Optional[str]
    role_type: Optional[str]
    menuid: Optional[str]
    parentid: Optional[str]
    bantuan: Optional[str]
    link: Optional[str]
    icon: Optional[str]
    kdlevel: Optional[int]
    is_show: Optional[int]
    created_at: Optional[datetime] = None
    created_by: Optional[str] = None
    updated_at: Optional[datetime] = None
    updated_by: Optional[str] = None
