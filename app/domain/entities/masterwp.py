from dataclasses import dataclass
from datetime import date, datetime
from typing import Optional


@dataclass
class MasterWp:
    idwp: Optional[int] = None
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
    created_at: Optional[datetime] = None
    created_by: Optional[str] = None
    updated_at: Optional[datetime] = None
    updated_by: Optional[str] = None
