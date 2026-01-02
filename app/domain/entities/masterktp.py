from dataclasses import dataclass
from datetime import date, datetime
from typing import Optional


@dataclass
class MasterKtp:
    idktp: Optional[int]
    nik: str
    nama: str
    nohp: str
    alamat: str
    idkabkokta: int
    idkecamatan: int
    idkelurahan: int
    agama: Optional[int] = None
    tgldaftar: Optional[date] = None
    idprovinsi: Optional[int] = None
    idrw: Optional[int] = None
    idrt: Optional[int] = None
    kdrt: Optional[str] = None
    nikah: Optional[int] = None
    tempatlahir: Optional[str] = None
    tgllahir: Optional[date] = None
    tglregistrasi: Optional[date] = None
    nokk: Optional[str] = None
    nobpjs: Optional[str] = None
    goldarah: Optional[str] = None
    email: Optional[str] = None
    pendidikan: Optional[str] = None
    jeniskelamin: Optional[str] = None
    dusun: Optional[str] = None
    pekerjaan: Optional[str] = None
    namaayah: Optional[str] = None
    namaibu: Optional[str] = None
    negara: Optional[str] = None
    statwn: Optional[str] = None
    statint: Optional[str] = None
    tglint: Optional[date] = None
    ket: Optional[str] = None
    created_at: Optional[datetime] = None
    created_by: Optional[str] = None
    updated_at: Optional[datetime] = None
    updated_by: Optional[str] = None
