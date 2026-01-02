from sqlalchemy.orm import Session

from app.domain.entities.masterwpdata import MasterWpData
from app.domain.repositories.masterwpdata_repository import MasterWpDataRepository
from app.infrastructure.orm.models import MasterWpData as MasterWpDataModel


class MasterWpDataRepositoryImpl(MasterWpDataRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return (
            self.db.query(MasterWpDataModel)
            .order_by(MasterWpDataModel.idwpdata.asc())
            .all()
        )

    def get_by_id(self, idwpdata: int):
        return (
            self.db.query(MasterWpDataModel)
            .filter(MasterWpDataModel.idwpdata == idwpdata)
            .first()
        )

    def create(self, master_wpdata: MasterWpData):
        db_master_wpdata = MasterWpDataModel(**master_wpdata.__dict__)
        self.db.add(db_master_wpdata)
        self.db.commit()
        self.db.refresh(db_master_wpdata)
        return db_master_wpdata

    def update(self, idwpdata: int, master_wpdata: MasterWpData):
        db_master_wpdata = self.get_by_id(idwpdata)
        if not db_master_wpdata:
            return None

        for key, value in master_wpdata.__dict__.items():
            if key == "idwpdata":
                continue
            if value is not None:
                setattr(db_master_wpdata, key, value)

        self.db.commit()
        self.db.refresh(db_master_wpdata)
        return db_master_wpdata

    def delete(self, idwpdata: int):
        db_master_wpdata = self.get_by_id(idwpdata)
        if not db_master_wpdata:
            return False
        self.db.delete(db_master_wpdata)
        self.db.commit()
        return True
