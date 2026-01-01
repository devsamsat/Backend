from sqlalchemy import (
    BigInteger,
    Boolean,
    Column,
    Date,
    DateTime,
    Integer,
    Numeric,
    String,
    Text,
    UniqueConstraint,
)
from sqlalchemy.sql import func
from app.core.database import Base

class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    full_name = Column(String)
    is_active = Column(Boolean, default=True)


class DynamicRecord(Base):
    __tablename__ = "dynamic_records"
    __table_args__ = (
        UniqueConstraint("table_name", "record_id", name="uniq_table_record"),
    )

    id = Column(Integer, primary_key=True)
    table_name = Column(String, nullable=False, index=True)
    record_id = Column(String, nullable=False, index=True)
    payload = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )


class AppGroupUser(Base):
    __tablename__ = "appgroupuser"

    kdgroup = Column(String(30), primary_key=True)
    nmgroup = Column(String(50), nullable=False)
    ket = Column(String(100))
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    created_by = Column(String(50))
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_by = Column(String(50))


class AppOtor(Base):
    __tablename__ = "appotor"

    kdgroup = Column(String(30), primary_key=True)
    roleid = Column(String(50), primary_key=True)
    ket = Column(String(100))
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    created_by = Column(String(50))
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_by = Column(String(50))


class AppRole(Base):
    __tablename__ = "approle"

    roleid = Column(String(50), primary_key=True)
    idapp = Column(BigInteger)
    role = Column(String(254))
    role_type = Column(String(2))
    menuid = Column(String(50))
    parentid = Column(String(50))
    bantuan = Column(String(254))
    link = Column(String(254))
    icon = Column(String(254))
    kdlevel = Column(Integer)
    is_show = Column(Integer)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    created_by = Column(String(50))
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_by = Column(String(50))


class AppUser(Base):
    __tablename__ = "appuser"

    userid = Column(String(50), primary_key=True)
    idupt = Column(BigInteger)
    kdtahap = Column(String(5), nullable=False)
    pwd = Column(String(200))
    idpeg = Column(BigInteger)
    kdgroup = Column(String(30), nullable=False)
    nik = Column(String(50))
    nama = Column(String(100))
    email = Column(String(50))
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    created_by = Column(String(50))
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_by = Column(String(50))


class JnsDok(Base):
    __tablename__ = "jnsdok"

    kddok = Column(String(10), primary_key=True)
    namadok = Column(String(30), nullable=False)
    keterangan = Column(String(200))
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    created_by = Column(String(50))
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_by = Column(String(50))


class JnsGolongan(Base):
    __tablename__ = "jnsgolongan"

    jnsgolid = Column(String(2), primary_key=True)
    golongan = Column(String(30), nullable=False)
    katid = Column(String(1))
    jnskendid = Column(String(3))
    viewall = Column(String(1))
    status = Column(String(1))
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    created_by = Column(String(50))
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_by = Column(String(50))


class JnsGuna(Base):
    __tablename__ = "jnsguna"

    kdguna = Column(String(2), primary_key=True)
    guna = Column(String(30), nullable=False)
    gunaplat = Column(String(2))
    progresif = Column(Numeric(18, 2))
    groupbpkb = Column(String(20), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    created_by = Column(String(50))
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_by = Column(String(50))


class MasterTarifNjop(Base):
    __tablename__ = "mastertarifnjop"

    idtarifnjop = Column(BigInteger, primary_key=True)
    iduunjop = Column(BigInteger, nullable=False)
    idrekd = Column(Integer)
    kdjnstarif = Column(String(3))
    namatarif = Column(String(200))
    idmerk = Column(Integer)
    tipe = Column(String(10))
    silinder = Column(String(50))
    tahun = Column(String(4))
    kodebbm = Column(String(10))
    njop = Column(Numeric(18, 2))
    status = Column(String(1))
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    created_by = Column(String(50))
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_by = Column(String(50))


class MasterTeks(Base):
    __tablename__ = "masterteks"

    idteks = Column(Integer, primary_key=True)
    datateks = Column(String(1024), nullable=False)
    status = Column(String(1), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    created_by = Column(String(50))
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_by = Column(String(50))


class MasterUpt(Base):
    __tablename__ = "masterupt"

    idupt = Column(BigInteger, primary_key=True)
    idparent = Column(BigInteger)
    kdupt = Column(String(50), nullable=False)
    nmupt = Column(String(500), nullable=False)
    kdlevel = Column(String(1))
    upt_type = Column(String(5), nullable=False)
    akroupt = Column(String(200))
    alamat = Column(String(200))
    telepon = Column(String(200))
    idbank = Column(Integer)
    idkabkota = Column(BigInteger)
    kepala = Column(BigInteger)
    koordinator = Column(BigInteger)
    bendahara = Column(BigInteger)
    norekb = Column(String(20))
    status = Column(String(1))
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    created_by = Column(String(50))
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_by = Column(String(50))


class MasterUuNjop(Base):
    __tablename__ = "masteruunjop"

    iduunjop = Column(BigInteger, primary_key=True)
    noperkada = Column(String(50))
    isiperkada = Column(String(200))
    tahun = Column(String(4))
    status = Column(String(1))
    keterangan = Column(String(200))
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    created_by = Column(String(50))
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_by = Column(String(50))


class MasterWp(Base):
    __tablename__ = "masterwp"

    idwp = Column(BigInteger, primary_key=True)
    objekbadanno = Column(String(30), nullable=False)
    namabadan = Column(String(100), nullable=False)
    idgroupusaha = Column(String(2))
    kodepolisi = Column(String(10))
    kodelokasi = Column(String(10))
    idbadan = Column(BigInteger)
    idklasifikasi = Column(String(2))
    idlokasi = Column(String(2))
    alamat = Column(String(255))
    idkabkokta = Column(BigInteger)
    idkecamatan = Column(BigInteger)
    idkelurahan = Column(BigInteger)
    idrw = Column(Integer)
    idrt = Column(Integer)
    telepon = Column(String(30))
    fax = Column(String(30))
    namapemilik = Column(String(50))
    idktp = Column(BigInteger)
    pekerjaan = Column(String(100))
    tgldaftar = Column(Date)
    tglsah = Column(Date)
    keteblokir = Column(String(255))
    tglhapus = Column(Date)
    groupblokir = Column(String(10))
    insidentil = Column(String(1), nullable=False)
    nopollama = Column(String(30), nullable=False)
    lastskp = Column(String(50))
    jnskendid = Column(String(3))
    idmerk = Column(Integer)
    merk = Column(String(30))
    tipe = Column(String(50))
    tahunbuat = Column(Integer)
    kodebbm = Column(String(10))
    bbm = Column(String(30))
    cylinder = Column(Integer)
    norangka = Column(String(50))
    nomesin = Column(String(50))
    nobpkb = Column(String(50))
    kdmilik = Column(String(2))
    kdguna = Column(String(2))
    kendke = Column(Integer)
    warna = Column(String(50))
    kdplat = Column(String(2), nullable=False)
    nostnkb = Column(String(50))
    daftarstnk = Column(String(50))
    tglcetakstnk = Column(Date)
    tglstnk = Column(Date)
    sdstnk = Column(Date)
    tglskp = Column(Date)
    awalskp = Column(Date)
    akhirskp = Column(Date)
    tglmutasi = Column(Date)
    tgljualbeli = Column(Date)
    nodaftar = Column(String(30))
    nosah1 = Column(String(20))
    tglsah1 = Column(Date)
    nosah2 = Column(String(20))
    tglsah2 = Column(Date)
    nosah3 = Column(String(20))
    tglsah3 = Column(Date)
    nosah4 = Column(String(20))
    tglsah4 = Column(Date)
    laporjual = Column(Date)
    nikpemilik = Column(String(30))
    notelppemilik = Column(String(30))
    putih = Column(String(1))
    status = Column(String(1))
    statint = Column(String(1))
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    created_by = Column(String(50))
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_by = Column(String(50))


class MasterWpData(Base):
    __tablename__ = "masterwpdata"

    idwpdata = Column(BigInteger, primary_key=True)
    idjnsd = Column(Integer, nullable=False)
    tglpendataan = Column(Date)
    idwp = Column(BigInteger, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    created_by = Column(String(50))
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_by = Column(String(50))


class TransDataKohir(Base):
    __tablename__ = "transdatakohir"

    idkohir = Column(BigInteger, primary_key=True)
    masaawal = Column(Date)
    masaakhir = Column(Date)
    tglpenetapan = Column(Date)
    penagih = Column(String(2), nullable=False)
    idwp = Column(BigInteger, nullable=False)
    tglkurangbayar = Column(Date)
    keterangan = Column(String(256))
    idupt = Column(BigInteger)
    skrupt = Column(String(20))
    validjr = Column(String(1))
    validjrby = Column(String(50))
    validpol = Column(String(1))
    validpolby = Column(String(50))
    ntpd = Column(String(50))
    tglntpd = Column(Date)
    idbank = Column(String(3))
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    created_by = Column(String(50))
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_by = Column(String(50))


class TransHistPendataan(Base):
    __tablename__ = "transhistpendataan"

    idhistpendataan = Column(BigInteger, primary_key=True)
    idpendataan = Column(BigInteger, nullable=False)
    spt = Column(String(8), nullable=False)
    idwpdata = Column(BigInteger, nullable=False)
    tglpendataan = Column(Date)
    masaawal = Column(Date)
    masaakhir = Column(Date)
    uruttgl = Column(Integer, nullable=False)
    jmlomzetawal = Column(Numeric(18, 2))
    tarifpjk = Column(Numeric(18, 2), nullable=False)
    idupt = Column(BigInteger, nullable=False)
    kdflow = Column(String(10))
    histid = Column(String(3), nullable=False)
    status = Column(String(1), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    created_by = Column(String(50))
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_by = Column(String(50))


class TransHistPendataanDet(Base):
    __tablename__ = "transhistpendataandet"

    idhistpendataandet = Column(BigInteger, primary_key=True)
    idhistpendataan = Column(BigInteger, nullable=False)
    idpenetapan = Column(BigInteger, nullable=False)
    nourut = Column(Integer, nullable=False)
    lokasi = Column(String(255))
    transid = Column(String(2), nullable=False)
    ket1 = Column(String(50), nullable=False)
    usahaid = Column(Integer, nullable=False)
    tarifpajak = Column(Numeric(18, 2), nullable=False)
    histid = Column(String(3), nullable=False)
    status = Column(String(1), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    created_by = Column(String(50))
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_by = Column(String(50))


class TransHistPenetapan(Base):
    __tablename__ = "transhistpenetapan"

    idhistpenetapan = Column(BigInteger, primary_key=True)
    idpenetapan = Column(BigInteger, nullable=False)
    idkohir = Column(BigInteger, nullable=False)
    nokohir = Column(String(30))
    idwpdata = Column(BigInteger, nullable=False)
    tglpenetapan = Column(Date)
    tgljatuhtempo = Column(Date)
    masaawal = Column(Date)
    masaakhir = Column(Date)
    uruttgl = Column(Integer, nullable=False)
    jmlomzetawal = Column(Numeric(18, 2))
    tarifpajak = Column(Numeric(18, 2), nullable=False)
    denda = Column(Numeric(18, 2))
    kenaikan = Column(Numeric(18, 2))
    statbayar = Column(String(1), nullable=False)
    tglbayar = Column(Date)
    jmlbayar = Column(Numeric(18, 2))
    tglkurangbayar = Column(Date)
    jmlkurangbayar = Column(Numeric(18, 2))
    jmlperingatan = Column(Integer)
    kdflow = Column(String(10))
    status = Column(String(1), nullable=False)
    opsid = Column(String(5))
    opsprov = Column(Numeric(18, 2))
    opskota = Column(Numeric(18, 2))
    dendaopsprov = Column(Numeric(18, 2))
    dendaopskota = Column(Numeric(18, 2))
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    created_by = Column(String(50))
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_by = Column(String(50))
