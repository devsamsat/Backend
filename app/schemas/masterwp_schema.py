from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel


class MasterWpCreate(BaseModel):
    objekbadanno: str
    namabadan: str
    insidentil: str
    nopollama: str
    kdplat: str
    idgroupusaha: Optional[str] = None
    kodepolisi: Optional[str] = None
    kodelokasi: Optional[str] = None
    idbadan: Optional[int] = None
    idklasifikasi: Optional[str] = None
    idlokasi: Optional[str] = None
    alamat: Optional[str] = None
    idkabkokta: Optional[int] = None
    idkecamatan: Optional[int] = None
    idkelurahan: Optional[int] = None
    idrw: Optional[int] = None
    idrt: Optional[int] = None
    telepon: Optional[str] = None
    fax: Optional[str] = None
    namapemilik: Optional[str] = None
    idktp: Optional[int] = None
    pekerjaan: Optional[str] = None
    tgldaftar: Optional[date] = None
    tglsah: Optional[date] = None
    keteblokir: Optional[str] = None
    tglhapus: Optional[date] = None
    groupblokir: Optional[str] = None
    lastskp: Optional[str] = None
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
    nostnkb: Optional[str] = None
    daftarstnk: Optional[str] = None
    tglcetakstnk: Optional[date] = None
    tglstnk: Optional[date] = None
    sdstnk: Optional[date] = None
    tglskp: Optional[date] = None
    awalskp: Optional[date] = None
    akhirskp: Optional[date] = None
    tglmutasi: Optional[date] = None
    tgljualbeli: Optional[date] = None
    nodaftar: Optional[str] = None
    nosah1: Optional[str] = None
    tglsah1: Optional[date] = None
    nosah2: Optional[str] = None
    tglsah2: Optional[date] = None
    nosah3: Optional[str] = None
    tglsah3: Optional[date] = None
    nosah4: Optional[str] = None
    tglsah4: Optional[date] = None
    laporjual: Optional[date] = None
    nikpemilik: Optional[str] = None
    notelppemilik: Optional[str] = None
    putih: Optional[str] = None
    status: Optional[str] = None
    statint: Optional[str] = None
    created_by: Optional[str] = None
    updated_by: Optional[str] = None


class MasterWpUpdate(BaseModel):
    objekbadanno: Optional[str] = None
    namabadan: Optional[str] = None
    insidentil: Optional[str] = None
    nopollama: Optional[str] = None
    kdplat: Optional[str] = None
    idgroupusaha: Optional[str] = None
    kodepolisi: Optional[str] = None
    kodelokasi: Optional[str] = None
    idbadan: Optional[int] = None
    idklasifikasi: Optional[str] = None
    idlokasi: Optional[str] = None
    alamat: Optional[str] = None
    idkabkokta: Optional[int] = None
    idkecamatan: Optional[int] = None
    idkelurahan: Optional[int] = None
    idrw: Optional[int] = None
    idrt: Optional[int] = None
    telepon: Optional[str] = None
    fax: Optional[str] = None
    namapemilik: Optional[str] = None
    idktp: Optional[int] = None
    pekerjaan: Optional[str] = None
    tgldaftar: Optional[date] = None
    tglsah: Optional[date] = None
    keteblokir: Optional[str] = None
    tglhapus: Optional[date] = None
    groupblokir: Optional[str] = None
    lastskp: Optional[str] = None
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
    nostnkb: Optional[str] = None
    daftarstnk: Optional[str] = None
    tglcetakstnk: Optional[date] = None
    tglstnk: Optional[date] = None
    sdstnk: Optional[date] = None
    tglskp: Optional[date] = None
    awalskp: Optional[date] = None
    akhirskp: Optional[date] = None
    tglmutasi: Optional[date] = None
    tgljualbeli: Optional[date] = None
    nodaftar: Optional[str] = None
    nosah1: Optional[str] = None
    tglsah1: Optional[date] = None
    nosah2: Optional[str] = None
    tglsah2: Optional[date] = None
    nosah3: Optional[str] = None
    tglsah3: Optional[date] = None
    nosah4: Optional[str] = None
    tglsah4: Optional[date] = None
    laporjual: Optional[date] = None
    nikpemilik: Optional[str] = None
    notelppemilik: Optional[str] = None
    putih: Optional[str] = None
    status: Optional[str] = None
    statint: Optional[str] = None
    updated_by: Optional[str] = None


class MasterWpResponse(BaseModel):
    idwp: int
    objekbadanno: str
    namabadan: str
    idgroupusaha: Optional[str]
    kodepolisi: Optional[str]
    kodelokasi: Optional[str]
    idbadan: Optional[int]
    idklasifikasi: Optional[str]
    idlokasi: Optional[str]
    alamat: Optional[str]
    idkabkokta: Optional[int]
    idkecamatan: Optional[int]
    idkelurahan: Optional[int]
    idrw: Optional[int]
    idrt: Optional[int]
    telepon: Optional[str]
    fax: Optional[str]
    namapemilik: Optional[str]
    idktp: Optional[int]
    pekerjaan: Optional[str]
    tgldaftar: Optional[date]
    tglsah: Optional[date]
    keteblokir: Optional[str]
    tglhapus: Optional[date]
    groupblokir: Optional[str]
    insidentil: str
    nopollama: str
    lastskp: Optional[str]
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
    kdplat: str
    nostnkb: Optional[str]
    daftarstnk: Optional[str]
    tglcetakstnk: Optional[date]
    tglstnk: Optional[date]
    sdstnk: Optional[date]
    tglskp: Optional[date]
    awalskp: Optional[date]
    akhirskp: Optional[date]
    tglmutasi: Optional[date]
    tgljualbeli: Optional[date]
    nodaftar: Optional[str]
    nosah1: Optional[str]
    tglsah1: Optional[date]
    nosah2: Optional[str]
    tglsah2: Optional[date]
    nosah3: Optional[str]
    tglsah3: Optional[date]
    nosah4: Optional[str]
    tglsah4: Optional[date]
    laporjual: Optional[date]
    nikpemilik: Optional[str]
    notelppemilik: Optional[str]
    putih: Optional[str]
    status: Optional[str]
    statint: Optional[str]
    created_at: datetime
    created_by: Optional[str]
    updated_at: datetime
    updated_by: Optional[str]

    class Config:
        from_attributes = True
