from sqlalchemy.orm import Session

from app.domain.entities.transwpdata import TransWpData
from app.domain.repositories.transwpdata_repository import TransWpDataRepository
from app.infrastructure.orm.models import TransWpData as TransWpDataModel


class TransWpDataRepositoryImpl(TransWpDataRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return (
            self.db.query(TransWpDataModel)
            .order_by(TransWpDataModel.idtwpdata.asc())
            .all()
        )

    def get_by_id(self, idtwpdata: int):
        return (
            self.db.query(TransWpDataModel)
            .filter(TransWpDataModel.idtwpdata == idtwpdata)
            .first()
        )

    def create(self, trans_wpdata: TransWpData):
        db_trans_wpdata = TransWpDataModel(**trans_wpdata.__dict__)
        self.db.add(db_trans_wpdata)
        self.db.commit()
        self.db.refresh(db_trans_wpdata)
        return db_trans_wpdata

    def update(self, idtwpdata: int, trans_wpdata: TransWpData):
        db_trans_wpdata = self.get_by_id(idtwpdata)
        if not db_trans_wpdata:
            return None

        for key, value in trans_wpdata.__dict__.items():
            if key == "idtwpdata":
                continue
            if value is not None:
                setattr(db_trans_wpdata, key, value)

        self.db.commit()
        self.db.refresh(db_trans_wpdata)
        return db_trans_wpdata

    def delete(self, idtwpdata: int):
        db_trans_wpdata = self.get_by_id(idtwpdata)
        if not db_trans_wpdata:
            return False
        self.db.delete(db_trans_wpdata)
        self.db.commit()
        return True
