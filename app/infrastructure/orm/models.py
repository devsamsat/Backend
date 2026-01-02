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


class MasterLibur(Base):
    __tablename__ = "masterlibur"

    idlibur = Column(Integer, primary_key=True)
    idkabkota = Column(BigInteger, nullable=False)
    level = Column(String(1), nullable=False)
    tanggal = Column(Date)
    namalibur = Column(String(150))
    keterangan = Column(String(3))
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    created_by = Column(String(50))
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_by = Column(String(50))


class MasterMerk(Base):
    __tablename__ = "mastermerk"

    idmerk = Column(Integer, primary_key=True)
    kdmerk = Column(String(2))
    nmmerk = Column(String(100), nullable=False)
    keterangan = Column(String(200))
    status = Column(String(1))
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    created_by = Column(String(50))
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_by = Column(String(50))


class MasterNpwpd(Base):
    __tablename__ = "masternpwpd"

    idnpwpd = Column(BigInteger, primary_key=True)
    statnpwpd = Column(String(1))
    npwpd = Column(String(50), nullable=False)
    idbadan = Column(BigInteger)
    idktp = Column(BigInteger)
    tgldaftar = Column(Date)
    nib = Column(String(50))
    namabadan = Column(String(100))
    alamat = Column(String(100))
    status = Column(String(1))
    ket = Column(String(512))
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    created_by = Column(String(50))
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_by = Column(String(50))


class MasterPegawai(Base):
    __tablename__ = "masterpegawai"

    idpegawai = Column(BigInteger, primary_key=True)
    idktp = Column(BigInteger)
    nip = Column(String(50), nullable=False)
    nik = Column(String(50))
    nama = Column(String(50), nullable=False)
    idupt = Column(BigInteger, nullable=False)
    status = Column(String(1), nullable=False)
    jabatan = Column(String(100))
    pangkat = Column(String(50))
    golongan = Column(String(20))
    uid = Column(String(15))
    telepon = Column(String(30))
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    created_by = Column(String(50))
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_by = Column(String(50))


class JnsHist(Base):
    __tablename__ = "jnshist"

    kdhist = Column(String(3), primary_key=True)
    nmhist = Column(String(50), nullable=False)
    kdflow = Column(String(2))
    status = Column(String(1))
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    created_by = Column(String(50))
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_by = Column(String(50))


class JnsJr(Base):
    __tablename__ = "jnsjr"

    jnsjrid = Column(String(2), primary_key=True)
    kodejr = Column(String(2), nullable=False)
    goljns = Column(String(2), nullable=False)
    pu = Column(String(2), nullable=False)
    roda = Column(Integer, nullable=False)
    keterangan = Column(String(200))
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    created_by = Column(String(50))
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_by = Column(String(50))


class JnsKatKendaraan(Base):
    __tablename__ = "jnskatkendaraan"

    katid = Column(String(1), primary_key=True)
    kendaraan = Column(String(30), nullable=False)
    jenisbpkb = Column(String(20), nullable=False)
    status = Column(String(1))
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    created_by = Column(String(50))
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_by = Column(String(50))


class JnsKendaraan(Base):
    __tablename__ = "jnskendaraan"

    jnskendid = Column(String(3), primary_key=True)
    jnskend = Column(String(30), nullable=False)
    katid = Column(String(1), nullable=False)
    jnsjrid = Column(String(2))
    golpjr = Column(Integer)
    golujr = Column(Integer)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    created_by = Column(String(50))
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_by = Column(String(50))


class JnsMilik(Base):
    __tablename__ = "jnsmilik"

    kdmilik = Column(String(2), primary_key=True)
    milik = Column(String(30), nullable=False)
    bpkpid = Column(String(2), nullable=False)
    status = Column(String(1))
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    created_by = Column(String(50))
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_by = Column(String(50))


class JnsPajak(Base):
    __tablename__ = "jnspajak"

    kdjnspjk = Column(String(2), primary_key=True)
    nmjnspjk = Column(String(50), nullable=False)
    keterangan = Column(String(200))
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    created_by = Column(String(50))
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_by = Column(String(50))


class JnsPlat(Base):
    __tablename__ = "jnsplat"

    kdplat = Column(String(2), primary_key=True)
    plat = Column(String(10), nullable=False)
    pu = Column(String(1), nullable=False)
    platjr = Column(Integer, nullable=False)
    numpkb = Column(Numeric(18, 4), nullable=False)
    numbbn1 = Column(Numeric(18, 4), nullable=False)
    numbbn2 = Column(Numeric(18, 4), nullable=False)
    umorg = Column(Numeric(18, 4), nullable=False)
    umbrg = Column(Numeric(18, 4), nullable=False)
    dnumpkb = Column(Numeric(18, 4), nullable=False)
    dnumbbn = Column(Numeric(18, 4), nullable=False)
    dumorg = Column(Numeric(18, 4), nullable=False)
    dumbrg = Column(Numeric(18, 4), nullable=False)
    abpkb = Column(Numeric(18, 4), nullable=False)
    abbbn1 = Column(Numeric(18, 4), nullable=False)
    abbbn2 = Column(Numeric(18, 4), nullable=False)
    numfiskal = Column(Numeric(18, 4), nullable=False)
    snid = Column(String(1), nullable=False)
    opspkb = Column(Numeric(18, 4), nullable=False)
    opsbbn = Column(Numeric(18, 4), nullable=False)
    opsnumpkb = Column(Numeric(18, 4), nullable=False)
    opsnumbbn1 = Column(Numeric(18, 4), nullable=False)
    opsnumbbn2 = Column(Numeric(18, 4), nullable=False)
    opsdnumpkb = Column(Numeric(18, 4), nullable=False)
    opsdnumbbn = Column(Numeric(18, 4), nullable=False)
    minnumpkb = Column(Numeric(18, 4), nullable=False)
    minnumbbn1 = Column(Numeric(18, 4), nullable=False)
    minnumbbn2 = Column(Numeric(18, 4), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    created_by = Column(String(50))
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_by = Column(String(50))


class JnsProgresif(Base):
    __tablename__ = "jnsprogresif"

    kdprogresif = Column(Integer, primary_key=True)
    progresifr2 = Column(Numeric(18, 2), nullable=False)
    progresifr4 = Column(Numeric(18, 2), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    created_by = Column(String(50))
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_by = Column(String(50))


class JnsRanmor(Base):
    __tablename__ = "jnsranmor"

    kdranmor = Column(String(1), primary_key=True)
    nmranmor = Column(String(30), nullable=False)
    snid = Column(String(1), nullable=False)
    status = Column(String(1))
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    created_by = Column(String(50))
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_by = Column(String(50))


class JnsStruRek(Base):
    __tablename__ = "jnsstrurek"

    mtglevel = Column(String(2), primary_key=True)
    nmlevel = Column(String(50), nullable=False)
    keterangan = Column(String(100), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    created_by = Column(String(50))
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_by = Column(String(50))


class JnsTarif(Base):
    __tablename__ = "jnstarif"

    kdjnstarif = Column(String(3), primary_key=True)
    nmjnstarif = Column(String(100), nullable=False)
    idupt = Column(BigInteger, nullable=False)
    jnskendid = Column(String(3))
    idrekd = Column(Integer)
    status = Column(String(1))
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    created_by = Column(String(50))
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_by = Column(String(50))


class JnsUmum(Base):
    __tablename__ = "jnsumum"

    kdumum = Column(String(2), primary_key=True)
    nmumum = Column(String(30), nullable=False)
    keterangan = Column(String(100), nullable=False)
    status = Column(String(1))
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    created_by = Column(String(50))
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_by = Column(String(50))


class MapJnsPendapatan(Base):
    __tablename__ = "mapjnspendapatan"

    idmapjnsd = Column(Integer, primary_key=True)
    nmjnspendapatan = Column(String(200), nullable=False)
    idrekpkb = Column(Integer)
    idrekbbnkb = Column(Integer)
    idrekopsenpkb = Column(Integer)
    idrekopsenbbnkb = Column(Integer)
    idrekpnbp = Column(Integer)
    keterangan = Column(String(200))
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    created_by = Column(String(50))
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_by = Column(String(50))


class MasterJnsPendapatan(Base):
    __tablename__ = "masterjnspendapatan"

    idjnsd = Column(Integer, primary_key=True)
    nmjnspendapatan = Column(String(200), nullable=False)
    parentid = Column(Integer)
    kdrek = Column(String(30))
    jatuhtempo = Column(Integer)
    status = Column(String(1))
    selfassessment = Column(String(1))
    katid = Column(String(1))
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    created_by = Column(String(50))
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_by = Column(String(50))


class MasterKabKota(Base):
    __tablename__ = "masterkabkota"

    idkabkota = Column(BigInteger, primary_key=True)
    idprovinsi = Column(BigInteger, nullable=False)
    kdkabkota = Column(String(10))
    nmkabkota = Column(String(50), nullable=False)
    akronim = Column(String(50), nullable=False)
    ibukota = Column(String(50), nullable=False)
    status = Column(String(1), nullable=False)
    bpkbid = Column(String(4), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    created_by = Column(String(50))
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_by = Column(String(50))


class MasterKabKotaAll(Base):
    __tablename__ = "masterkabkotaall"

    idkabkotaall = Column(BigInteger, primary_key=True)
    idprovinsi = Column(BigInteger, nullable=False)
    kdkabkota = Column(String(8))
    nmkabkota = Column(String(100), nullable=False)
    status = Column(String(1), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    created_by = Column(String(50))
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_by = Column(String(50))


class MasterKaupt(Base):
    __tablename__ = "masterkaupt"

    idkaupt = Column(BigInteger, primary_key=True)
    idpegawai = Column(BigInteger)
    idupt = Column(BigInteger, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    created_by = Column(String(50))
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_by = Column(String(50))


class MasterKb(Base):
    __tablename__ = "masterkb"

    idkb = Column(BigInteger, primary_key=True)
    nomorfaktur = Column(String(30))
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


class MasterKbDet(Base):
    __tablename__ = "masterkbdet"

    idkbdet = Column(BigInteger, primary_key=True)
    idkb = Column(BigInteger, nullable=False)
    idjnsd = Column(Integer, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    created_by = Column(String(50))
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_by = Column(String(50))


class MasterKecamatan(Base):
    __tablename__ = "masterkecamatan"

    idkecamatan = Column(BigInteger, primary_key=True)
    idkabkota = Column(BigInteger, nullable=False)
    kdkecamatan = Column(String(10))
    nmkecamatan = Column(String(100), nullable=False)
    alamat = Column(String(100), nullable=False)
    telepon = Column(String(30), nullable=False)
    fax = Column(String(30))
    status = Column(String(1), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    created_by = Column(String(50))
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_by = Column(String(50))


class MasterKelurahan(Base):
    __tablename__ = "masterkelurahan"

    idkelurahan = Column(BigInteger, primary_key=True)
    idkecamatan = Column(BigInteger, nullable=False)
    kdkelurahan = Column(String(10))
    nmkelurahan = Column(String(100), nullable=False)
    alamat = Column(String(100), nullable=False)
    telepon = Column(String(30), nullable=False)
    kodepos = Column(String(30))
    status = Column(String(1), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    created_by = Column(String(50))
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_by = Column(String(50))


class MasterKiosk(Base):
    __tablename__ = "masterkiosk"

    idkios = Column(Integer, primary_key=True)
    idparent = Column(Integer)
    kodekiosk = Column(String(20), nullable=False)
    datakiosk = Column(String(200), nullable=False)
    level = Column(String(1), nullable=False)
    status = Column(String(1), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    created_by = Column(String(50))
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_by = Column(String(50))


class MasterKtp(Base):
    __tablename__ = "masterktp"

    idktp = Column(BigInteger, primary_key=True)
    nik = Column(String(50), nullable=False)
    nama = Column(String(100), nullable=False)
    agama = Column(Integer)
    nohp = Column(String(30), nullable=False)
    alamat = Column(String(255), nullable=False)
    tgldaftar = Column(Date)
    idprovinsi = Column(BigInteger)
    idkabkokta = Column(BigInteger, nullable=False)
    idkecamatan = Column(BigInteger, nullable=False)
    idkelurahan = Column(BigInteger, nullable=False)
    idrw = Column(Integer)
    idrt = Column(Integer)
    kdrt = Column(String(20))
    nikah = Column(Integer)
    tempatlahir = Column(String(100))
    tgllahir = Column(Date)
    tglregistrasi = Column(Date)
    nokk = Column(String(30))
    nobpjs = Column(String(30))
    goldarah = Column(String(2))
    email = Column(String(50))
    pendidikan = Column(String(50))
    jeniskelamin = Column(String(1))
    dusun = Column(String(50))
    pekerjaan = Column(String(100))
    namaayah = Column(String(100))
    namaibu = Column(String(100))
    negara = Column(String(50))
    statwn = Column(String(1))
    statint = Column(String(1))
    tglint = Column(Date)
    ket = Column(String(512))
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    created_by = Column(String(50))
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_by = Column(String(50))


class MasterProvinsi(Base):
    __tablename__ = "masterprovinsi"

    idprovinsi = Column(BigInteger, primary_key=True)
    kdprovinsi = Column(String(10), nullable=False)
    nmprovinsi = Column(String(100), nullable=False)
    status = Column(String(1), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    created_by = Column(String(50))
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_by = Column(String(50))


class MasterRekd(Base):
    __tablename__ = "masterrekd"

    idrekd = Column(Integer, primary_key=True)
    idparent = Column(Integer)
    mtglevel = Column(String(2))
    kdrek = Column(String(30), nullable=False)
    nmrek = Column(String(200))
    kdjnspjk = Column(String(2))
    rek_type = Column(String(1))
    status = Column(String(1))
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    created_by = Column(String(50))
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_by = Column(String(50))


class MasterRekNrc(Base):
    __tablename__ = "masterreknrc"

    idreknrc = Column(Integer, primary_key=True)
    mtglevel = Column(String(2))
    kdrek = Column(String(30), nullable=False)
    nmrek = Column(String(500))
    rek_type = Column(String(1))
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    created_by = Column(String(50))
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_by = Column(String(50))


class MasterRt(Base):
    __tablename__ = "masterrt"

    idrt = Column(Integer, primary_key=True)
    idrw = Column(Integer, nullable=False)
    kdrt = Column(String(10))
    status = Column(String(1), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    created_by = Column(String(50))
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_by = Column(String(50))


class MasterRw(Base):
    __tablename__ = "masterrw"

    idrw = Column(Integer, primary_key=True)
    idkelurahan = Column(BigInteger, nullable=False)
    kdrw = Column(String(10))
    alamat = Column(String(100), nullable=False)
    status = Column(String(1), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    created_by = Column(String(50))
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_by = Column(String(50))


class MasterTarif(Base):
    __tablename__ = "mastertarif"

    idtarif = Column(BigInteger, primary_key=True)
    kdjnspjk = Column(String(2), nullable=False)
    jnskendid = Column(String(3))
    satuan = Column(String(200))
    awal = Column(Numeric(18, 2))
    akhir = Column(Numeric(18, 2))
    keterangan = Column(String(200))
    kdflow = Column(String(10))
    kdplat = Column(String(2))
    statumum = Column(String(1))
    tarif = Column(Numeric(18, 2))
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    created_by = Column(String(50))
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_by = Column(String(50))
