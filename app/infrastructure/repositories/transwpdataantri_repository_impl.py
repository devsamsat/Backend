from sqlalchemy.orm import Session

from app.domain.entities.transwpdataantri import TransWpDataAntri
from app.domain.repositories.transwpdataantri_repository import TransWpDataAntriRepository
from app.infrastructure.orm.models import TransWpDataAntri as TransWpDataAntriModel


class TransWpDataAntriRepositoryImpl(TransWpDataAntriRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return (
            self.db.query(TransWpDataAntriModel)
            .order_by(TransWpDataAntriModel.idantri.asc())
            .all()
        )

    def get_by_id(self, idantri: int):
        return (
            self.db.query(TransWpDataAntriModel)
            .filter(TransWpDataAntriModel.idantri == idantri)
            .first()
        )

    def create(self, trans_wpdataantri: TransWpDataAntri):
        db_trans_wpdataantri = TransWpDataAntriModel(**trans_wpdataantri.__dict__)
        self.db.add(db_trans_wpdataantri)
        self.db.commit()
        self.db.refresh(db_trans_wpdataantri)
        return db_trans_wpdataantri

    def update(self, idantri: int, trans_wpdataantri: TransWpDataAntri):
        db_trans_wpdataantri = self.get_by_id(idantri)
        if not db_trans_wpdataantri:
            return None

        for key, value in trans_wpdataantri.__dict__.items():
            if key == "idantri":
                continue
            if value is not None:
                setattr(db_trans_wpdataantri, key, value)

        self.db.commit()
        self.db.refresh(db_trans_wpdataantri)
        return db_trans_wpdataantri

    def delete(self, idantri: int):
        db_trans_wpdataantri = self.get_by_id(idantri)
        if not db_trans_wpdataantri:
            return False
        self.db.delete(db_trans_wpdataantri)
        self.db.commit()
        return True
