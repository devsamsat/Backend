from sqlalchemy.orm import Session

from app.domain.entities.masterjabttd import MasterJabTtd
from app.domain.repositories.masterjabttd_repository import MasterJabTtdRepository
from app.infrastructure.orm.models import MasterJabTtd as MasterJabTtdModel


class MasterJabTtdRepositoryImpl(MasterJabTtdRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(MasterJabTtdModel).order_by(MasterJabTtdModel.idjabttd.asc()).all()

    def get_by_id(self, idjabttd: int):
        return (
            self.db.query(MasterJabTtdModel)
            .filter(MasterJabTtdModel.idjabttd == idjabttd)
            .first()
        )

    def create(self, master_jab_ttd: MasterJabTtd):
        db_master_jab_ttd = MasterJabTtdModel(**master_jab_ttd.__dict__)
        self.db.add(db_master_jab_ttd)
        self.db.commit()
        self.db.refresh(db_master_jab_ttd)
        return db_master_jab_ttd

    def update(self, idjabttd: int, master_jab_ttd: MasterJabTtd):
        db_master_jab_ttd = self.get_by_id(idjabttd)
        if not db_master_jab_ttd:
            return None

        for key, value in master_jab_ttd.__dict__.items():
            if key == "idjabttd":
                continue
            if value is not None:
                setattr(db_master_jab_ttd, key, value)

        self.db.commit()
        self.db.refresh(db_master_jab_ttd)
        return db_master_jab_ttd

    def delete(self, idjabttd: int):
        db_master_jab_ttd = self.get_by_id(idjabttd)
        if not db_master_jab_ttd:
            return False
        self.db.delete(db_master_jab_ttd)
        self.db.commit()
        return True
