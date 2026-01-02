from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel


class MasterKtpCreate(BaseModel):
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
    created_by: Optional[str] = None
    updated_by: Optional[str] = None


class MasterKtpUpdate(BaseModel):
    nik: Optional[str] = None
    nama: Optional[str] = None
    nohp: Optional[str] = None
    alamat: Optional[str] = None
    idkabkokta: Optional[int] = None
    idkecamatan: Optional[int] = None
    idkelurahan: Optional[int] = None
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
    updated_by: Optional[str] = None


class MasterKtpResponse(BaseModel):
    idktp: int
    nik: str
    nama: str
    nohp: str
    alamat: str
    idkabkokta: int
    idkecamatan: int
    idkelurahan: int
    agama: Optional[int]
    tgldaftar: Optional[date]
    idprovinsi: Optional[int]
    idrw: Optional[int]
    idrt: Optional[int]
    kdrt: Optional[str]
    nikah: Optional[int]
    tempatlahir: Optional[str]
    tgllahir: Optional[date]
    tglregistrasi: Optional[date]
    nokk: Optional[str]
    nobpjs: Optional[str]
    goldarah: Optional[str]
    email: Optional[str]
    pendidikan: Optional[str]
    jeniskelamin: Optional[str]
    dusun: Optional[str]
    pekerjaan: Optional[str]
    namaayah: Optional[str]
    namaibu: Optional[str]
    negara: Optional[str]
    statwn: Optional[str]
    statint: Optional[str]
    tglint: Optional[date]
    ket: Optional[str]
    created_at: datetime
    created_by: Optional[str]
    updated_at: datetime
    updated_by: Optional[str]

    class Config:
        from_attributes = True
