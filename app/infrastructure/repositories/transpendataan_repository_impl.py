from sqlalchemy.orm import Session

from app.domain.entities.transpendataan import TransPendataan
from app.domain.repositories.transpendataan_repository import TransPendataanRepository
from app.infrastructure.orm.models import TransPendataan as TransPendataanModel


class TransPendataanRepositoryImpl(TransPendataanRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return (
            self.db.query(TransPendataanModel)
            .order_by(TransPendataanModel.idpendataan.asc())
            .all()
        )

    def get_by_id(self, idpendataan: int):
        return (
            self.db.query(TransPendataanModel)
            .filter(TransPendataanModel.idpendataan == idpendataan)
            .first()
        )

    def create(self, trans_pendataan: TransPendataan):
        db_trans_pendataan = TransPendataanModel(**trans_pendataan.__dict__)
        self.db.add(db_trans_pendataan)
        self.db.commit()
        self.db.refresh(db_trans_pendataan)
        return db_trans_pendataan

    def update(self, idpendataan: int, trans_pendataan: TransPendataan):
        db_trans_pendataan = self.get_by_id(idpendataan)
        if not db_trans_pendataan:
            return None

        for key, value in trans_pendataan.__dict__.items():
            if key == "idpendataan":
                continue
            if value is not None:
                setattr(db_trans_pendataan, key, value)

        self.db.commit()
        self.db.refresh(db_trans_pendataan)
        return db_trans_pendataan

    def delete(self, idpendataan: int):
        db_trans_pendataan = self.get_by_id(idpendataan)
        if not db_trans_pendataan:
            return False
        self.db.delete(db_trans_pendataan)
        self.db.commit()
        return True
