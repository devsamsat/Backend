from sqlalchemy.orm import Session

from app.domain.entities.masterwp import MasterWp
from app.domain.repositories.masterwp_repository import MasterWpRepository
from app.infrastructure.orm.models import MasterWp as MasterWpModel


class MasterWpRepositoryImpl(MasterWpRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(MasterWpModel).order_by(MasterWpModel.idwp.asc()).all()

    def get_by_id(self, idwp: int):
        return self.db.query(MasterWpModel).filter(MasterWpModel.idwp == idwp).first()

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
