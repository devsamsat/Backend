from sqlalchemy.orm import Session

from app.domain.entities.masterprovinsi import MasterProvinsi
from app.domain.repositories.masterprovinsi_repository import MasterProvinsiRepository
from app.infrastructure.orm.models import MasterProvinsi as MasterProvinsiModel


class MasterProvinsiRepositoryImpl(MasterProvinsiRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return (
            self.db.query(MasterProvinsiModel)
            .order_by(MasterProvinsiModel.idprovinsi.asc())
            .all()
        )

    def get_by_id(self, idprovinsi: int):
        return (
            self.db.query(MasterProvinsiModel)
            .filter(MasterProvinsiModel.idprovinsi == idprovinsi)
            .first()
        )

    def create(self, master_provinsi: MasterProvinsi):
        db_master_provinsi = MasterProvinsiModel(**master_provinsi.__dict__)
        self.db.add(db_master_provinsi)
        self.db.commit()
        self.db.refresh(db_master_provinsi)
        return db_master_provinsi

    def update(self, idprovinsi: int, master_provinsi: MasterProvinsi):
        db_master_provinsi = self.get_by_id(idprovinsi)
        if not db_master_provinsi:
            return None

        for key, value in master_provinsi.__dict__.items():
            if key == "idprovinsi":
                continue
            if value is not None:
                setattr(db_master_provinsi, key, value)

        self.db.commit()
        self.db.refresh(db_master_provinsi)
        return db_master_provinsi

    def delete(self, idprovinsi: int):
        db_master_provinsi = self.get_by_id(idprovinsi)
        if not db_master_provinsi:
            return False
        self.db.delete(db_master_provinsi)
        self.db.commit()
        return True
