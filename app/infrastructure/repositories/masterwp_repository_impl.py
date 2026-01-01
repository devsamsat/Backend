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

    def create(self, wp: MasterWp):
        db_wp = MasterWpModel(**wp.__dict__)
        self.db.add(db_wp)
        self.db.commit()
        self.db.refresh(db_wp)
        return db_wp

    def update(self, idwp: int, wp: MasterWp):
        db_wp = self.get_by_id(idwp)
        if not db_wp:
            return None

        for key, value in wp.__dict__.items():
            if key == "idwp":
                continue
            if value is not None:
                setattr(db_wp, key, value)

        self.db.commit()
        self.db.refresh(db_wp)
        return db_wp

    def delete(self, idwp: int):
        db_wp = self.get_by_id(idwp)
        if not db_wp:
            return False
        self.db.delete(db_wp)
        self.db.commit()
        return True
