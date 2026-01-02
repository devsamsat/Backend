from sqlalchemy.orm import Session

from app.domain.entities.transhistpendataandet import TransHistPendataanDet
from app.domain.repositories.transhistpendataandet_repository import (
    TransHistPendataanDetRepository,
)
from app.infrastructure.orm.models import (
    TransHistPendataanDet as TransHistPendataanDetModel,
)


class TransHistPendataanDetRepositoryImpl(TransHistPendataanDetRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return (
            self.db.query(TransHistPendataanDetModel)
            .order_by(TransHistPendataanDetModel.idhistpendataandet.asc())
            .all()
        )

    def get_by_id(self, idhistpendataandet: int):
        return (
            self.db.query(TransHistPendataanDetModel)
            .filter(TransHistPendataanDetModel.idhistpendataandet == idhistpendataandet)
            .first()
        )

    def create(self, trans_hist_pendataan_det: TransHistPendataanDet):
        db_trans_hist_pendataan_det = TransHistPendataanDetModel(
            **trans_hist_pendataan_det.__dict__
        )
        self.db.add(db_trans_hist_pendataan_det)
        self.db.commit()
        self.db.refresh(db_trans_hist_pendataan_det)
        return db_trans_hist_pendataan_det

    def update(
        self,
        idhistpendataandet: int,
        trans_hist_pendataan_det: TransHistPendataanDet,
    ):
        db_trans_hist_pendataan_det = self.get_by_id(idhistpendataandet)
        if not db_trans_hist_pendataan_det:
            return None

        for key, value in trans_hist_pendataan_det.__dict__.items():
            if key == "idhistpendataandet":
                continue
            if value is not None:
                setattr(db_trans_hist_pendataan_det, key, value)

        self.db.commit()
        self.db.refresh(db_trans_hist_pendataan_det)
        return db_trans_hist_pendataan_det

    def delete(self, idhistpendataandet: int):
        db_trans_hist_pendataan_det = self.get_by_id(idhistpendataandet)
        if not db_trans_hist_pendataan_det:
            return False
        self.db.delete(db_trans_hist_pendataan_det)
        self.db.commit()
        return True
