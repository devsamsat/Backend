from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class AppUserCreate(BaseModel):
    userid: str
    kdtahap: str
    kdgroup: str
    idupt: Optional[int] = None
    pwd: Optional[str] = None
    idpeg: Optional[int] = None
    nik: Optional[str] = None
    nama: Optional[str] = None
    email: Optional[str] = None
    created_by: Optional[str] = None
    updated_by: Optional[str] = None


class AppUserUpdate(BaseModel):
    idupt: Optional[int] = None
    kdtahap: Optional[str] = None
    pwd: Optional[str] = None
    idpeg: Optional[int] = None
    kdgroup: Optional[str] = None
    nik: Optional[str] = None
    nama: Optional[str] = None
    email: Optional[str] = None
    updated_by: Optional[str] = None


class AppUserResponse(BaseModel):
    userid: str
    idupt: Optional[int]
    kdtahap: str
    pwd: Optional[str]
    idpeg: Optional[int]
    kdgroup: str
    nik: Optional[str]
    nama: Optional[str]
    email: Optional[str]
    created_at: datetime
    created_by: Optional[str]
    updated_at: datetime
    updated_by: Optional[str]

    class Config:
        from_attributes = True
