from dataclasses import dataclass
from datetime import date, datetime
from typing import Optional


@dataclass
class MasterAb:
    idab: Optional[int]
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
    created_at: Optional[datetime] = None
    created_by: Optional[str] = None
    updated_at: Optional[datetime] = None
    updated_by: Optional[str] = None
