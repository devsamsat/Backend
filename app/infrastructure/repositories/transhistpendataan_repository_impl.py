from sqlalchemy.orm import Session

from app.domain.entities.transhistpendataan import TransHistPendataan
from app.domain.repositories.transhistpendataan_repository import (
    TransHistPendataanRepository,
)
from app.infrastructure.orm.models import TransHistPendataan as TransHistPendataanModel


class TransHistPendataanRepositoryImpl(TransHistPendataanRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return (
            self.db.query(TransHistPendataanModel)
            .order_by(TransHistPendataanModel.idhistpendataan.asc())
            .all()
        )

    def get_by_id(self, idhistpendataan: int):
        return (
            self.db.query(TransHistPendataanModel)
            .filter(TransHistPendataanModel.idhistpendataan == idhistpendataan)
            .first()
        )

    def create(self, trans_hist_pendataan: TransHistPendataan):
        db_trans_hist_pendataan = TransHistPendataanModel(**trans_hist_pendataan.__dict__)
        self.db.add(db_trans_hist_pendataan)
        self.db.commit()
        self.db.refresh(db_trans_hist_pendataan)
        return db_trans_hist_pendataan

    def update(self, idhistpendataan: int, trans_hist_pendataan: TransHistPendataan):
        db_trans_hist_pendataan = self.get_by_id(idhistpendataan)
        if not db_trans_hist_pendataan:
            return None

        for key, value in trans_hist_pendataan.__dict__.items():
            if key == "idhistpendataan":
                continue
            if value is not None:
                setattr(db_trans_hist_pendataan, key, value)

        self.db.commit()
        self.db.refresh(db_trans_hist_pendataan)
        return db_trans_hist_pendataan

    def delete(self, idhistpendataan: int):
        db_trans_hist_pendataan = self.get_by_id(idhistpendataan)
        if not db_trans_hist_pendataan:
            return False
        self.db.delete(db_trans_hist_pendataan)
        self.db.commit()
        return True
