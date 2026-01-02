from sqlalchemy.orm import Session

from app.domain.entities.masterkecamatan import MasterKecamatan
from app.domain.repositories.masterkecamatan_repository import MasterKecamatanRepository
from app.infrastructure.orm.models import MasterKecamatan as MasterKecamatanModel


class MasterKecamatanRepositoryImpl(MasterKecamatanRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return (
            self.db.query(MasterKecamatanModel)
            .order_by(MasterKecamatanModel.idkecamatan.asc())
            .all()
        )

    def get_by_id(self, idkecamatan: int):
        return (
            self.db.query(MasterKecamatanModel)
            .filter(MasterKecamatanModel.idkecamatan == idkecamatan)
            .first()
        )

    def create(self, master_kecamatan: MasterKecamatan):
        db_master_kecamatan = MasterKecamatanModel(**master_kecamatan.__dict__)
        self.db.add(db_master_kecamatan)
        self.db.commit()
        self.db.refresh(db_master_kecamatan)
        return db_master_kecamatan

    def update(self, idkecamatan: int, master_kecamatan: MasterKecamatan):
        db_master_kecamatan = self.get_by_id(idkecamatan)
        if not db_master_kecamatan:
            return None

        for key, value in master_kecamatan.__dict__.items():
            if key == "idkecamatan":
                continue
            if value is not None:
                setattr(db_master_kecamatan, key, value)

        self.db.commit()
        self.db.refresh(db_master_kecamatan)
        return db_master_kecamatan

    def delete(self, idkecamatan: int):
        db_master_kecamatan = self.get_by_id(idkecamatan)
        if not db_master_kecamatan:
            return False
        self.db.delete(db_master_kecamatan)
        self.db.commit()
        return True
