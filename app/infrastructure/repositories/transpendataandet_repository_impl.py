from sqlalchemy.orm import Session

from app.domain.entities.transpendataandet import TransPendataanDet
from app.domain.repositories.transpendataandet_repository import (
    TransPendataanDetRepository,
)
from app.infrastructure.orm.models import TransPendataanDet as TransPendataanDetModel


class TransPendataanDetRepositoryImpl(TransPendataanDetRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return (
            self.db.query(TransPendataanDetModel)
            .order_by(TransPendataanDetModel.idpendataandet.asc())
            .all()
        )

    def get_by_id(self, idpendataandet: int):
        return (
            self.db.query(TransPendataanDetModel)
            .filter(TransPendataanDetModel.idpendataandet == idpendataandet)
            .first()
        )

    def create(self, trans_pendataan_det: TransPendataanDet):
        db_trans_pendataan_det = TransPendataanDetModel(**trans_pendataan_det.__dict__)
        self.db.add(db_trans_pendataan_det)
        self.db.commit()
        self.db.refresh(db_trans_pendataan_det)
        return db_trans_pendataan_det

    def update(self, idpendataandet: int, trans_pendataan_det: TransPendataanDet):
        db_trans_pendataan_det = self.get_by_id(idpendataandet)
        if not db_trans_pendataan_det:
            return None

        for key, value in trans_pendataan_det.__dict__.items():
            if key == "idpendataandet":
                continue
            if value is not None:
                setattr(db_trans_pendataan_det, key, value)

        self.db.commit()
        self.db.refresh(db_trans_pendataan_det)
        return db_trans_pendataan_det

    def delete(self, idpendataandet: int):
        db_trans_pendataan_det = self.get_by_id(idpendataandet)
        if not db_trans_pendataan_det:
            return False
        self.db.delete(db_trans_pendataan_det)
        self.db.commit()
        return True
