from sqlalchemy.orm import Session

from app.domain.entities.masterupt import MasterUpt
from app.domain.repositories.masterupt_repository import MasterUptRepository
from app.infrastructure.orm.models import MasterUpt as MasterUptModel


class MasterUptRepositoryImpl(MasterUptRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(MasterUptModel).order_by(MasterUptModel.idupt.asc()).all()

    def get_by_id(self, idupt: int):
        return (
            self.db.query(MasterUptModel)
            .filter(MasterUptModel.idupt == idupt)
            .first()
        )

    def create(self, master_upt: MasterUpt):
        db_master_upt = MasterUptModel(**master_upt.__dict__)
        self.db.add(db_master_upt)
        self.db.commit()
        self.db.refresh(db_master_upt)
        return db_master_upt

    def update(self, idupt: int, master_upt: MasterUpt):
        db_master_upt = self.get_by_id(idupt)
        if not db_master_upt:
            return None

        for key, value in master_upt.__dict__.items():
            if key == "idupt":
                continue
            if value is not None:
                setattr(db_master_upt, key, value)

        self.db.commit()
        self.db.refresh(db_master_upt)
        return db_master_upt

    def delete(self, idupt: int):
        db_master_upt = self.get_by_id(idupt)
        if not db_master_upt:
            return False
        self.db.delete(db_master_upt)
        self.db.commit()
        return True
