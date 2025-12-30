from sqlalchemy.orm import Session

from app.domain.entities.masterbbm import MasterBbm
from app.domain.repositories.masterbbm_repository import MasterBbmRepository
from app.infrastructure.orm.models import MasterBbm as MasterBbmModel


class MasterBbmRepositoryImpl(MasterBbmRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(MasterBbmModel).order_by(MasterBbmModel.kodebbm.asc()).all()

    def get_by_id(self, kodebbm: str):
        return self.db.query(MasterBbmModel).filter(MasterBbmModel.kodebbm == kodebbm).first()

    def create(self, master_bbm: MasterBbm):
        db_master_bbm = MasterBbmModel(**master_bbm.__dict__)
        self.db.add(db_master_bbm)
        self.db.commit()
        self.db.refresh(db_master_bbm)
        return db_master_bbm

    def update(self, kodebbm: str, master_bbm: MasterBbm):
        db_master_bbm = self.get_by_id(kodebbm)
        if not db_master_bbm:
            return None

        for key, value in master_bbm.__dict__.items():
            if key == "kodebbm":
                continue
            if value is not None:
                setattr(db_master_bbm, key, value)

        self.db.commit()
        self.db.refresh(db_master_bbm)
        return db_master_bbm

    def delete(self, kodebbm: str):
        db_master_bbm = self.get_by_id(kodebbm)
        if not db_master_bbm:
            return False
        self.db.delete(db_master_bbm)
        self.db.commit()
        return True
