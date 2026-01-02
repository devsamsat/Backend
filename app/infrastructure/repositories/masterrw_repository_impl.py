from sqlalchemy.orm import Session

from app.domain.entities.masterrw import MasterRw
from app.domain.repositories.masterrw_repository import MasterRwRepository
from app.infrastructure.orm.models import MasterRw as MasterRwModel


class MasterRwRepositoryImpl(MasterRwRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(MasterRwModel).order_by(MasterRwModel.idrw.asc()).all()

    def get_by_id(self, idrw: int):
        return self.db.query(MasterRwModel).filter(MasterRwModel.idrw == idrw).first()

    def create(self, master_rw: MasterRw):
        db_master_rw = MasterRwModel(**master_rw.__dict__)
        self.db.add(db_master_rw)
        self.db.commit()
        self.db.refresh(db_master_rw)
        return db_master_rw

    def update(self, idrw: int, master_rw: MasterRw):
        db_master_rw = self.get_by_id(idrw)
        if not db_master_rw:
            return None

        for key, value in master_rw.__dict__.items():
            if key == "idrw":
                continue
            if value is not None:
                setattr(db_master_rw, key, value)

        self.db.commit()
        self.db.refresh(db_master_rw)
        return db_master_rw

    def delete(self, idrw: int):
        db_master_rw = self.get_by_id(idrw)
        if not db_master_rw:
            return False
        self.db.delete(db_master_rw)
        self.db.commit()
        return True
