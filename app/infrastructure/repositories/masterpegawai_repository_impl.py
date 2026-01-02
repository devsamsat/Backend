from sqlalchemy.orm import Session

from app.domain.entities.masterpegawai import MasterPegawai
from app.domain.repositories.masterpegawai_repository import MasterPegawaiRepository
from app.infrastructure.orm.models import MasterPegawai as MasterPegawaiModel


class MasterPegawaiRepositoryImpl(MasterPegawaiRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(MasterPegawaiModel).order_by(MasterPegawaiModel.idpegawai.asc()).all()

    def get_by_id(self, idpegawai: int):
        return (
            self.db.query(MasterPegawaiModel)
            .filter(MasterPegawaiModel.idpegawai == idpegawai)
            .first()
        )

    def create(self, master_pegawai: MasterPegawai):
        db_record = MasterPegawaiModel(**master_pegawai.__dict__)
        self.db.add(db_record)
        self.db.commit()
        self.db.refresh(db_record)
        return db_record

    def update(self, idpegawai: int, master_pegawai: MasterPegawai):
        db_record = self.get_by_id(idpegawai)
        if not db_record:
            return None

        for key, value in master_pegawai.__dict__.items():
            if key == "idpegawai":
                continue
            if value is not None:
                setattr(db_record, key, value)

        self.db.commit()
        self.db.refresh(db_record)
        return db_record

    def delete(self, idpegawai: int):
        db_record = self.get_by_id(idpegawai)
        if not db_record:
            return False
        self.db.delete(db_record)
        self.db.commit()
        return True
