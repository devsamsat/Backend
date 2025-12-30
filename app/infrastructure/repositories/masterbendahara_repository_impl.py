from sqlalchemy.orm import Session

from app.domain.entities.masterbendahara import MasterBendahara
from app.domain.repositories.masterbendahara_repository import MasterBendaharaRepository
from app.infrastructure.orm.models import MasterBendahara as MasterBendaharaModel


class MasterBendaharaRepositoryImpl(MasterBendaharaRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(MasterBendaharaModel).order_by(MasterBendaharaModel.idbend.asc()).all()

    def get_by_id(self, idbend: int):
        return self.db.query(MasterBendaharaModel).filter(MasterBendaharaModel.idbend == idbend).first()

    def create(self, master_bendahara: MasterBendahara):
        db_master_bendahara = MasterBendaharaModel(**master_bendahara.__dict__)
        self.db.add(db_master_bendahara)
        self.db.commit()
        self.db.refresh(db_master_bendahara)
        return db_master_bendahara

    def update(self, idbend: int, master_bendahara: MasterBendahara):
        db_master_bendahara = self.get_by_id(idbend)
        if not db_master_bendahara:
            return None

        for key, value in master_bendahara.__dict__.items():
            if key == "idbend":
                continue
            if value is not None:
                setattr(db_master_bendahara, key, value)

        self.db.commit()
        self.db.refresh(db_master_bendahara)
        return db_master_bendahara

    def delete(self, idbend: int):
        db_master_bendahara = self.get_by_id(idbend)
        if not db_master_bendahara:
            return False
        self.db.delete(db_master_bendahara)
        self.db.commit()
        return True
