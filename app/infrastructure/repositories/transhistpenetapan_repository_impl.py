from sqlalchemy.orm import Session

from app.domain.entities.transhistpenetapan import TransHistPenetapan
from app.domain.repositories.transhistpenetapan_repository import (
    TransHistPenetapanRepository,
)
from app.infrastructure.orm.models import TransHistPenetapan as TransHistPenetapanModel


class TransHistPenetapanRepositoryImpl(TransHistPenetapanRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return (
            self.db.query(TransHistPenetapanModel)
            .order_by(TransHistPenetapanModel.idhistpenetapan.asc())
            .all()
        )

    def get_by_id(self, idhistpenetapan: int):
        return (
            self.db.query(TransHistPenetapanModel)
            .filter(TransHistPenetapanModel.idhistpenetapan == idhistpenetapan)
            .first()
        )

    def create(self, trans_hist_penetapan: TransHistPenetapan):
        db_trans_hist_penetapan = TransHistPenetapanModel(**trans_hist_penetapan.__dict__)
        self.db.add(db_trans_hist_penetapan)
        self.db.commit()
        self.db.refresh(db_trans_hist_penetapan)
        return db_trans_hist_penetapan

    def update(self, idhistpenetapan: int, trans_hist_penetapan: TransHistPenetapan):
        db_trans_hist_penetapan = self.get_by_id(idhistpenetapan)
        if not db_trans_hist_penetapan:
            return None

        for key, value in trans_hist_penetapan.__dict__.items():
            if key == "idhistpenetapan":
                continue
            if value is not None:
                setattr(db_trans_hist_penetapan, key, value)

        self.db.commit()
        self.db.refresh(db_trans_hist_penetapan)
        return db_trans_hist_penetapan

    def delete(self, idhistpenetapan: int):
        db_trans_hist_penetapan = self.get_by_id(idhistpenetapan)
        if not db_trans_hist_penetapan:
            return False
        self.db.delete(db_trans_hist_penetapan)
        self.db.commit()
        return True
