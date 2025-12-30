from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class AppRoleCreate(BaseModel):
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
    created_by: Optional[str] = None
    updated_by: Optional[str] = None


class AppRoleUpdate(BaseModel):
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
    created_by: Optional[str] = None
    updated_by: Optional[str] = None


class AppRoleResponse(BaseModel):
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
    created_at: datetime
    created_by: Optional[str]
    updated_at: datetime
    updated_by: Optional[str]

    class Config:
        from_attributes = True
