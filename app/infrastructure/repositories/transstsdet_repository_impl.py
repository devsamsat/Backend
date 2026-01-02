from sqlalchemy.orm import Session

from app.domain.entities.transstsdet import TransStsDet
from app.domain.repositories.transstsdet_repository import TransStsDetRepository
from app.infrastructure.orm.models import TransStsDet as TransStsDetModel


class TransStsDetRepositoryImpl(TransStsDetRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return (
            self.db.query(TransStsDetModel)
            .order_by(TransStsDetModel.idstsdet.asc())
            .all()
        )

    def get_by_id(self, idstsdet: int):
        return (
            self.db.query(TransStsDetModel)
            .filter(TransStsDetModel.idstsdet == idstsdet)
            .first()
        )

    def create(self, trans_sts_det: TransStsDet):
        db_trans_sts_det = TransStsDetModel(**trans_sts_det.__dict__)
        self.db.add(db_trans_sts_det)
        self.db.commit()
        self.db.refresh(db_trans_sts_det)
        return db_trans_sts_det

    def update(self, idstsdet: int, trans_sts_det: TransStsDet):
        db_trans_sts_det = self.get_by_id(idstsdet)
        if not db_trans_sts_det:
            return None

        for key, value in trans_sts_det.__dict__.items():
            if key == "idstsdet":
                continue
            if value is not None:
                setattr(db_trans_sts_det, key, value)

        self.db.commit()
        self.db.refresh(db_trans_sts_det)
        return db_trans_sts_det

    def delete(self, idstsdet: int):
        db_trans_sts_det = self.get_by_id(idstsdet)
        if not db_trans_sts_det:
            return False
        self.db.delete(db_trans_sts_det)
        self.db.commit()
        return True
