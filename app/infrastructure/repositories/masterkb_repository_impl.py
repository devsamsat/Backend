from sqlalchemy.orm import Session

from app.domain.entities.masterkb import MasterKb
from app.domain.repositories.masterkb_repository import MasterKbRepository
from app.infrastructure.orm.models import MasterKb as MasterKbModel


class MasterKbRepositoryImpl(MasterKbRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(MasterKbModel).order_by(MasterKbModel.idkb.asc()).all()

    def get_by_id(self, idkb: int):
        return self.db.query(MasterKbModel).filter(MasterKbModel.idkb == idkb).first()

    def create(self, master_kb: MasterKb):
        db_master_kb = MasterKbModel(**master_kb.__dict__)
        self.db.add(db_master_kb)
        self.db.commit()
        self.db.refresh(db_master_kb)
        return db_master_kb

    def update(self, idkb: int, master_kb: MasterKb):
        db_master_kb = self.get_by_id(idkb)
        if not db_master_kb:
            return None

        for key, value in master_kb.__dict__.items():
            if key == "idkb":
                continue
            if value is not None:
                setattr(db_master_kb, key, value)

        self.db.commit()
        self.db.refresh(db_master_kb)
        return db_master_kb

    def delete(self, idkb: int):
        db_master_kb = self.get_by_id(idkb)
        if not db_master_kb:
            return False
        self.db.delete(db_master_kb)
        self.db.commit()
        return True
