from sqlalchemy.orm import Session

from app.domain.entities.masterkiosk import MasterKiosk
from app.domain.repositories.masterkiosk_repository import MasterKioskRepository
from app.infrastructure.orm.models import MasterKiosk as MasterKioskModel


class MasterKioskRepositoryImpl(MasterKioskRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(MasterKioskModel).order_by(MasterKioskModel.idkios.asc()).all()

    def get_by_id(self, idkios: int):
        return (
            self.db.query(MasterKioskModel)
            .filter(MasterKioskModel.idkios == idkios)
            .first()
        )

    def create(self, master_kiosk: MasterKiosk):
        db_master_kiosk = MasterKioskModel(**master_kiosk.__dict__)
        self.db.add(db_master_kiosk)
        self.db.commit()
        self.db.refresh(db_master_kiosk)
        return db_master_kiosk

    def update(self, idkios: int, master_kiosk: MasterKiosk):
        db_master_kiosk = self.get_by_id(idkios)
        if not db_master_kiosk:
            return None

        for key, value in master_kiosk.__dict__.items():
            if key == "idkios":
                continue
            if value is not None:
                setattr(db_master_kiosk, key, value)

        self.db.commit()
        self.db.refresh(db_master_kiosk)
        return db_master_kiosk

    def delete(self, idkios: int):
        db_master_kiosk = self.get_by_id(idkios)
        if not db_master_kiosk:
            return False
        self.db.delete(db_master_kiosk)
        self.db.commit()
        return True
