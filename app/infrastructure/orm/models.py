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


class MasterAb(Base):
    __tablename__ = "masterab"

    idab = Column(BigInteger, primary_key=True)
    nomorab = Column(String(30), nullable=False)
    namabadan = Column(String(100), nullable=False)
    alamat = Column(String(255))
    idkabkokta = Column(BigInteger)
    idkecamatan = Column(BigInteger)
    idkelurahan = Column(BigInteger)
    idrw = Column(Integer)
    idrt = Column(Integer)
    telepon = Column(String(30))
    fax = Column(String(30))
    idktp = Column(BigInteger)
    noktp = Column(String(30))
    pekerjaan = Column(String(50))
    tgldaftar = Column(Date)
    tglfaktur = Column(Date)
    insidentil = Column(String(1), nullable=False)
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
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    created_by = Column(String(50))
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_by = Column(String(50))


class MasterAbDet(Base):
    __tablename__ = "masterabdet"

    idabdet = Column(BigInteger, primary_key=True)
    idab = Column(BigInteger, nullable=False)
    idjnsd = Column(Integer, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    created_by = Column(String(50))
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_by = Column(String(50))


class MasterBadan(Base):
    __tablename__ = "masterbadan"

    idbadan = Column(BigInteger, primary_key=True)
    nib = Column(String(50))
    idktp = Column(BigInteger)
    namabadan = Column(String(100), nullable=False)
    nohp = Column(String(30), nullable=False)
    alamat = Column(String(255), nullable=False)
    tgldaftar = Column(Date)
    idprovinsi = Column(BigInteger)
    idkabkokta = Column(BigInteger)
    ket = Column(String(512))
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    created_by = Column(String(50))
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_by = Column(String(50))


class MasterBank(Base):
    __tablename__ = "masterbank"

    idbank = Column(Integer, primary_key=True)
    kodebank = Column(String(10), nullable=False)
    namabank = Column(String(100), nullable=False)
    akronimbank = Column(String(50))
    cabangbank = Column(String(50))
    alamatbank = Column(String(100))
    status = Column(String(1))
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    created_by = Column(String(50))
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_by = Column(String(50))


class MasterBbm(Base):
    __tablename__ = "masterbbm"

    kodebbm = Column(String(10), primary_key=True)
    namabbm = Column(String(50), nullable=False)
    keterangan = Column(String(100))
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    created_by = Column(String(50))
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_by = Column(String(50))


class MasterBendahara(Base):
    __tablename__ = "masterbendahara"

    idbend = Column(BigInteger, primary_key=True)
    idpegawai = Column(BigInteger, nullable=False)
    idbank = Column(Integer, nullable=False)
    norek = Column(String(50), nullable=False)
    namarek = Column(String(100), nullable=False)
    jnsbend = Column(String(2), nullable=False)
    status = Column(String(1), nullable=False)
    jabatan = Column(String(100))
    pangkat = Column(String(50))
    uid = Column(String(15))
    koordinator = Column(BigInteger)
    idreknrc = Column(Integer)
    telepon = Column(String(30))
    ket = Column(String(200))
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    created_by = Column(String(50))
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_by = Column(String(50))


class MasterFlow(Base):
    __tablename__ = "masterflow"

    kdflow = Column(String(10), primary_key=True)
    nmflow = Column(String(100), nullable=False)
    pkb = Column(String(2))
    bbn1 = Column(String(2))
    bbn2 = Column(String(2))
    swd = Column(String(2))
    atbkend = Column(String(1))
    flowjr = Column(String(1))
    stnkbaru = Column(String(2))
    tnkb = Column(String(2))
    sahstnk = Column(String(2))
    perpanjangstnk = Column(String(2))
    potongan = Column(String(2))
    bataslayanan = Column(Integer)
    satuan = Column(String(50))
    status = Column(String(1))
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    created_by = Column(String(50))
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_by = Column(String(50))


class MasterHapusDenda(Base):
    __tablename__ = "masterhapusdenda"

    idhapusdenda = Column(Integer, primary_key=True)
    jenis = Column(String(1), nullable=False)
    uraian = Column(String(100), nullable=False)
    awal = Column(Date)
    akhir = Column(Date)
    nilai = Column(Numeric(18, 2))
    satuan = Column(String(30))
    ket = Column(String(256))
    status = Column(String(1))
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    created_by = Column(String(50))
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_by = Column(String(50))


class MasterHistory(Base):
    __tablename__ = "masterhistory"

    idhistory = Column(BigInteger, primary_key=True)
    idwp = Column(BigInteger, nullable=False)
    objekbadanno = Column(String(30), nullable=False)
    namabadan = Column(String(100), nullable=False)
    idgroupusaha = Column(String(2))
    kodepolisi = Column(String(10))
    kodelokasi = Column(String(30))
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
    histid = Column(String(3), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    created_by = Column(String(50))
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_by = Column(String(50))


class MasterJabTtd(Base):
    __tablename__ = "masterjabttd"

    idjabttd = Column(BigInteger, primary_key=True)
    idpegawai = Column(BigInteger, nullable=False)
    kddok = Column(String(10), nullable=False)
    jabatan = Column(String(50))
    ket = Column(String(256))
    status = Column(String(1))
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    created_by = Column(String(50))
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_by = Column(String(50))
