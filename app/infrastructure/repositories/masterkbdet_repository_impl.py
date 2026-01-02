from sqlalchemy.orm import Session

from app.domain.entities.masterkbdet import MasterKbDet
from app.domain.repositories.masterkbdet_repository import MasterKbDetRepository
from app.infrastructure.orm.models import MasterKbDet as MasterKbDetModel


class MasterKbDetRepositoryImpl(MasterKbDetRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return (
            self.db.query(MasterKbDetModel)
            .order_by(MasterKbDetModel.idkbdet.asc())
            .all()
        )

    def get_by_id(self, idkbdet: int):
        return (
            self.db.query(MasterKbDetModel)
            .filter(MasterKbDetModel.idkbdet == idkbdet)
            .first()
        )

    def create(self, master_kbdet: MasterKbDet):
        db_master_kbdet = MasterKbDetModel(**master_kbdet.__dict__)
        self.db.add(db_master_kbdet)
        self.db.commit()
        self.db.refresh(db_master_kbdet)
        return db_master_kbdet

    def update(self, idkbdet: int, master_kbdet: MasterKbDet):
        db_master_kbdet = self.get_by_id(idkbdet)
        if not db_master_kbdet:
            return None

        for key, value in master_kbdet.__dict__.items():
            if key == "idkbdet":
                continue
            if value is not None:
                setattr(db_master_kbdet, key, value)

        self.db.commit()
        self.db.refresh(db_master_kbdet)
        return db_master_kbdet

    def delete(self, idkbdet: int):
        db_master_kbdet = self.get_by_id(idkbdet)
        if not db_master_kbdet:
            return False
        self.db.delete(db_master_kbdet)
        self.db.commit()
        return True
