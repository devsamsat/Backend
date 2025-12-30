from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel


class MasterAbCreate(BaseModel):
    nomorab: str
    namabadan: str
    insidentil: str
    kdplat: str
    alamat: Optional[str] = None
    idkabkokta: Optional[int] = None
    idkecamatan: Optional[int] = None
    idkelurahan: Optional[int] = None
    idrw: Optional[int] = None
    idrt: Optional[int] = None
    telepon: Optional[str] = None
    fax: Optional[str] = None
    idktp: Optional[int] = None
    noktp: Optional[str] = None
    pekerjaan: Optional[str] = None
    tgldaftar: Optional[date] = None
    tglfaktur: Optional[date] = None
    jnskendid: Optional[str] = None
    idmerk: Optional[int] = None
    merk: Optional[str] = None
    tipe: Optional[str] = None
    tahunbuat: Optional[int] = None
    kodebbm: Optional[str] = None
    bbm: Optional[str] = None
    cylinder: Optional[int] = None
    norangka: Optional[str] = None
    nomesin: Optional[str] = None
    nobpkb: Optional[str] = None
    kdmilik: Optional[str] = None
    kdguna: Optional[str] = None
    kendke: Optional[int] = None
    warna: Optional[str] = None
    created_by: Optional[str] = None
    updated_by: Optional[str] = None


class MasterAbUpdate(BaseModel):
    nomorab: Optional[str] = None
    namabadan: Optional[str] = None
    insidentil: Optional[str] = None
    kdplat: Optional[str] = None
    alamat: Optional[str] = None
    idkabkokta: Optional[int] = None
    idkecamatan: Optional[int] = None
    idkelurahan: Optional[int] = None
    idrw: Optional[int] = None
    idrt: Optional[int] = None
    telepon: Optional[str] = None
    fax: Optional[str] = None
    idktp: Optional[int] = None
    noktp: Optional[str] = None
    pekerjaan: Optional[str] = None
    tgldaftar: Optional[date] = None
    tglfaktur: Optional[date] = None
    jnskendid: Optional[str] = None
    idmerk: Optional[int] = None
    merk: Optional[str] = None
    tipe: Optional[str] = None
    tahunbuat: Optional[int] = None
    kodebbm: Optional[str] = None
    bbm: Optional[str] = None
    cylinder: Optional[int] = None
    norangka: Optional[str] = None
    nomesin: Optional[str] = None
    nobpkb: Optional[str] = None
    kdmilik: Optional[str] = None
    kdguna: Optional[str] = None
    kendke: Optional[int] = None
    warna: Optional[str] = None
    updated_by: Optional[str] = None


class MasterAbResponse(BaseModel):
    idab: int
    nomorab: str
    namabadan: str
    insidentil: str
    kdplat: str
    alamat: Optional[str]
    idkabkokta: Optional[int]
    idkecamatan: Optional[int]
    idkelurahan: Optional[int]
    idrw: Optional[int]
    idrt: Optional[int]
    telepon: Optional[str]
    fax: Optional[str]
    idktp: Optional[int]
    noktp: Optional[str]
    pekerjaan: Optional[str]
    tgldaftar: Optional[date]
    tglfaktur: Optional[date]
    jnskendid: Optional[str]
    idmerk: Optional[int]
    merk: Optional[str]
    tipe: Optional[str]
    tahunbuat: Optional[int]
    kodebbm: Optional[str]
    bbm: Optional[str]
    cylinder: Optional[int]
    norangka: Optional[str]
    nomesin: Optional[str]
    nobpkb: Optional[str]
    kdmilik: Optional[str]
    kdguna: Optional[str]
    kendke: Optional[int]
    warna: Optional[str]
    created_at: datetime
    created_by: Optional[str]
    updated_at: datetime
    updated_by: Optional[str]

    class Config:
        from_attributes = True
