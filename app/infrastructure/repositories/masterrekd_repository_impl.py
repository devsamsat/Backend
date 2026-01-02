from sqlalchemy.orm import Session

from app.domain.entities.masterrekd import MasterRekd
from app.domain.repositories.masterrekd_repository import MasterRekdRepository
from app.infrastructure.orm.models import MasterRekd as MasterRekdModel


class MasterRekdRepositoryImpl(MasterRekdRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(MasterRekdModel).order_by(MasterRekdModel.idrekd.asc()).all()

    def get_by_id(self, idrekd: int):
        return self.db.query(MasterRekdModel).filter(MasterRekdModel.idrekd == idrekd).first()

    def create(self, master_rekd: MasterRekd):
        db_master_rekd = MasterRekdModel(**master_rekd.__dict__)
        self.db.add(db_master_rekd)
        self.db.commit()
        self.db.refresh(db_master_rekd)
        return db_master_rekd

    def update(self, idrekd: int, master_rekd: MasterRekd):
        db_master_rekd = self.get_by_id(idrekd)
        if not db_master_rekd:
            return None

        for key, value in master_rekd.__dict__.items():
            if key == "idrekd":
                continue
            if value is not None:
                setattr(db_master_rekd, key, value)

        self.db.commit()
        self.db.refresh(db_master_rekd)
        return db_master_rekd

    def delete(self, idrekd: int):
        db_master_rekd = self.get_by_id(idrekd)
        if not db_master_rekd:
            return False
        self.db.delete(db_master_rekd)
        self.db.commit()
        return True
