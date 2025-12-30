from sqlalchemy.orm import Session

from app.domain.entities.masterab import MasterAb
from app.domain.repositories.masterab_repository import MasterAbRepository
from app.infrastructure.orm.models import MasterAb as MasterAbModel


class MasterAbRepositoryImpl(MasterAbRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(MasterAbModel).order_by(MasterAbModel.idab.asc()).all()

    def get_by_id(self, idab: int):
        return self.db.query(MasterAbModel).filter(MasterAbModel.idab == idab).first()

    def create(self, master_ab: MasterAb):
        db_master_ab = MasterAbModel(**master_ab.__dict__)
        self.db.add(db_master_ab)
        self.db.commit()
        self.db.refresh(db_master_ab)
        return db_master_ab

    def update(self, idab: int, master_ab: MasterAb):
        db_master_ab = self.get_by_id(idab)
        if not db_master_ab:
            return None

        for key, value in master_ab.__dict__.items():
            if key == "idab":
                continue
            if value is not None:
                setattr(db_master_ab, key, value)

        self.db.commit()
        self.db.refresh(db_master_ab)
        return db_master_ab

    def delete(self, idab: int):
        db_master_ab = self.get_by_id(idab)
        if not db_master_ab:
            return False
        self.db.delete(db_master_ab)
        self.db.commit()
        return True
