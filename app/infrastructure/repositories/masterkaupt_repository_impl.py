from sqlalchemy.orm import Session

from app.domain.entities.masterkaupt import MasterKaupt
from app.domain.repositories.masterkaupt_repository import MasterKauptRepository
from app.infrastructure.orm.models import MasterKaupt as MasterKauptModel


class MasterKauptRepositoryImpl(MasterKauptRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(MasterKauptModel).order_by(MasterKauptModel.idkaupt.asc()).all()

    def get_by_id(self, idkaupt: int):
        return (
            self.db.query(MasterKauptModel)
            .filter(MasterKauptModel.idkaupt == idkaupt)
            .first()
        )

    def create(self, master_kaupt: MasterKaupt):
        db_master_kaupt = MasterKauptModel(**master_kaupt.__dict__)
        self.db.add(db_master_kaupt)
        self.db.commit()
        self.db.refresh(db_master_kaupt)
        return db_master_kaupt

    def update(self, idkaupt: int, master_kaupt: MasterKaupt):
        db_master_kaupt = self.get_by_id(idkaupt)
        if not db_master_kaupt:
            return None

        for key, value in master_kaupt.__dict__.items():
            if key == "idkaupt":
                continue
            if value is not None:
                setattr(db_master_kaupt, key, value)

        self.db.commit()
        self.db.refresh(db_master_kaupt)
        return db_master_kaupt

    def delete(self, idkaupt: int):
        db_master_kaupt = self.get_by_id(idkaupt)
        if not db_master_kaupt:
            return False
        self.db.delete(db_master_kaupt)
        self.db.commit()
        return True
