from sqlalchemy.orm import Session

from app.domain.entities.masternpwpd import MasterNpwpd
from app.domain.repositories.masternpwpd_repository import MasterNpwpdRepository
from app.infrastructure.orm.models import MasterNpwpd as MasterNpwpdModel


class MasterNpwpdRepositoryImpl(MasterNpwpdRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(MasterNpwpdModel).order_by(MasterNpwpdModel.idnpwpd.asc()).all()

    def get_by_id(self, idnpwpd: int):
        return self.db.query(MasterNpwpdModel).filter(MasterNpwpdModel.idnpwpd == idnpwpd).first()

    def create(self, master_npwpd: MasterNpwpd):
        db_record = MasterNpwpdModel(**master_npwpd.__dict__)
        self.db.add(db_record)
        self.db.commit()
        self.db.refresh(db_record)
        return db_record

    def update(self, idnpwpd: int, master_npwpd: MasterNpwpd):
        db_record = self.get_by_id(idnpwpd)
        if not db_record:
            return None

        for key, value in master_npwpd.__dict__.items():
            if key == "idnpwpd":
                continue
            if value is not None:
                setattr(db_record, key, value)

        self.db.commit()
        self.db.refresh(db_record)
        return db_record

    def delete(self, idnpwpd: int):
        db_record = self.get_by_id(idnpwpd)
        if not db_record:
            return False
        self.db.delete(db_record)
        self.db.commit()
        return True
