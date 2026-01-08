from sqlalchemy import or_
from sqlalchemy.orm import Session

from app.domain.entities.masterwp import MasterWp
from app.domain.repositories.masterwp_repository import MasterWpRepository
from app.infrastructure.orm.models import (
    MasterKabKota,
    MasterKecamatan,
    MasterKelurahan,
    MasterWp as MasterWpModel,
)


class MasterWpRepositoryImpl(MasterWpRepository):

    def __init__(self, db: Session):
        self.db = db

    def _base_query_with_names(self):
        return (
            self.db.query(
                MasterWpModel,
                MasterKelurahan.nmkelurahan.label("nmkelurahan"),
                MasterKecamatan.nmkecamatan.label("nmkecamatan"),
                MasterKabKota.nmkabkota.label("nmkabkota"),
            )
            .outerjoin(
                MasterKelurahan,
                MasterWpModel.idkelurahan == MasterKelurahan.idkelurahan,
            )
            .outerjoin(
                MasterKecamatan,
                MasterWpModel.idkecamatan == MasterKecamatan.idkecamatan,
            )
            .outerjoin(
                MasterKabKota,
                MasterWpModel.idkabkokta == MasterKabKota.idkabkota,
            )
        )

    def _attach_location_names(self, rows):
        results = []
        for master_wp, nmkelurahan, nmkecamatan, nmkabkota in rows:
            setattr(master_wp, "nmkelurahan", nmkelurahan)
            setattr(master_wp, "nmkecamatan", nmkecamatan)
            setattr(master_wp, "nmkabkota", nmkabkota)
            results.append(master_wp)
        return results

    def get_all(self, filters: dict | None = None, page: int | None = None, limit: int | None = None):
        query = self._base_query_with_names()

        if filters:
            nopollama = filters.get("nopollama")
            namapemilik = filters.get("namapemilik")
            nikpemilik = filters.get("nikpemilik")
            alamat = filters.get("alamat")
            kelurahan = filters.get("kelurahan")
            kecamatan = filters.get("kecamatan")
            objekbadanno = filters.get("objekbadanno")
            nostnkb = filters.get("nostnkb")
            nobpkb = filters.get("nobpkb")
            tgljualbeli = filters.get("tgljualbeli")
            tgldaftar = filters.get("tgldaftar")
            norangka = filters.get("norangka")
            nomesin = filters.get("nomesin")
            warna = filters.get("warna")
            is_match = bool(filters.get("is_match"))

            if nopollama:
                if is_match:
                    query = query.filter(MasterWpModel.nopollama == nopollama)
                else:
                    query = query.filter(MasterWpModel.nopollama.ilike(f"%{nopollama}%"))
            if namapemilik:
                if is_match:
                    query = query.filter(MasterWpModel.namapemilik == namapemilik)
                else:
                    query = query.filter(MasterWpModel.namapemilik.ilike(f"%{namapemilik}%"))
            if nikpemilik:
                idktp_value = None
                try:
                    idktp_value = int(nikpemilik)
                except ValueError:
                    idktp_value = None
                if is_match:
                    conditions = [MasterWpModel.nikpemilik == nikpemilik]
                else:
                    conditions = [MasterWpModel.nikpemilik.ilike(f"%{nikpemilik}%")]
                if idktp_value is not None:
                    conditions.append(MasterWpModel.idktp == idktp_value)
                query = query.filter(or_(*conditions))
            if alamat:
                if is_match:
                    query = query.filter(MasterWpModel.alamat == alamat)
                else:
                    query = query.filter(MasterWpModel.alamat.ilike(f"%{alamat}%"))
            if kelurahan:
                if is_match:
                    query = query.filter(MasterKelurahan.nmkelurahan == kelurahan)
                else:
                    query = query.filter(MasterKelurahan.nmkelurahan.ilike(f"%{kelurahan}%"))
            if kecamatan:
                if is_match:
                    query = query.filter(MasterKecamatan.nmkecamatan == kecamatan)
                else:
                    query = query.filter(MasterKecamatan.nmkecamatan.ilike(f"%{kecamatan}%"))
            if objekbadanno:
                if is_match:
                    query = query.filter(MasterWpModel.objekbadanno == objekbadanno)
                else:
                    query = query.filter(MasterWpModel.objekbadanno.ilike(f"%{objekbadanno}%"))
            if nostnkb:
                if is_match:
                    query = query.filter(MasterWpModel.nostnkb == nostnkb)
                else:
                    query = query.filter(MasterWpModel.nostnkb.ilike(f"%{nostnkb}%"))
            if nobpkb:
                if is_match:
                    query = query.filter(MasterWpModel.nobpkb == nobpkb)
                else:
                    query = query.filter(MasterWpModel.nobpkb.ilike(f"%{nobpkb}%"))
            if tgljualbeli:
                query = query.filter(MasterWpModel.tgljualbeli == tgljualbeli)
            if tgldaftar:
                query = query.filter(MasterWpModel.tgldaftar == tgldaftar)
            if norangka:
                if is_match:
                    query = query.filter(MasterWpModel.norangka == norangka)
                else:
                    query = query.filter(MasterWpModel.norangka.ilike(f"%{norangka}%"))
            if nomesin:
                if is_match:
                    query = query.filter(MasterWpModel.nomesin == nomesin)
                else:
                    query = query.filter(MasterWpModel.nomesin.ilike(f"%{nomesin}%"))
            if warna:
                if is_match:
                    query = query.filter(MasterWpModel.warna == warna)
                else:
                    query = query.filter(MasterWpModel.warna.ilike(f"%{warna}%"))

        query = query.order_by(MasterWpModel.idwp.asc())

        if limit is not None:
            page_number = page or 1
            offset = (page_number - 1) * limit
            query = query.offset(offset).limit(limit)

        return self._attach_location_names(query.all())

    def get_by_id(self, idwp: int):
        row = self._base_query_with_names().filter(MasterWpModel.idwp == idwp).first()
        if not row:
            return None
        master_wp, nmkelurahan, nmkecamatan, nmkabkota = row
        setattr(master_wp, "nmkelurahan", nmkelurahan)
        setattr(master_wp, "nmkecamatan", nmkecamatan)
        setattr(master_wp, "nmkabkota", nmkabkota)
        return master_wp

    def create(self, master_wp: MasterWp):
        db_master_wp = MasterWpModel(**master_wp.__dict__)
        self.db.add(db_master_wp)
        self.db.commit()
        self.db.refresh(db_master_wp)
        return db_master_wp

    def update(self, idwp: int, master_wp: MasterWp):
        db_master_wp = self.get_by_id(idwp)
        if not db_master_wp:
            return None

        for key, value in master_wp.__dict__.items():
            if key == "idwp":
                continue
            if value is not None:
                setattr(db_master_wp, key, value)

        self.db.commit()
        self.db.refresh(db_master_wp)
        return db_master_wp

    def delete(self, idwp: int):
        db_master_wp = self.get_by_id(idwp)
        if not db_master_wp:
            return False
        self.db.delete(db_master_wp)
        self.db.commit()
        return True
