from sqlalchemy.orm import Session

from app.domain.entities.masterbadan import MasterBadan
from app.domain.repositories.masterbadan_repository import MasterBadanRepository
from app.infrastructure.orm.models import MasterBadan as MasterBadanModel


class MasterBadanRepositoryImpl(MasterBadanRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(MasterBadanModel).order_by(MasterBadanModel.idbadan.asc()).all()

    def get_by_id(self, idbadan: int):
        return self.db.query(MasterBadanModel).filter(MasterBadanModel.idbadan == idbadan).first()

    def create(self, master_badan: MasterBadan):
        db_master_badan = MasterBadanModel(**master_badan.__dict__)
        self.db.add(db_master_badan)
        self.db.commit()
        self.db.refresh(db_master_badan)
        return db_master_badan

    def update(self, idbadan: int, master_badan: MasterBadan):
        db_master_badan = self.get_by_id(idbadan)
        if not db_master_badan:
            return None

        for key, value in master_badan.__dict__.items():
            if key == "idbadan":
                continue
            if value is not None:
                setattr(db_master_badan, key, value)

        self.db.commit()
        self.db.refresh(db_master_badan)
        return db_master_badan

    def delete(self, idbadan: int):
        db_master_badan = self.get_by_id(idbadan)
        if not db_master_badan:
            return False
        self.db.delete(db_master_badan)
        self.db.commit()
        return True
