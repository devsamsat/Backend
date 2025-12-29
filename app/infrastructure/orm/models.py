from sqlalchemy import BigInteger, Boolean, Column, DateTime, Integer, String, Text, UniqueConstraint
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
