from sqlalchemy.orm import Session

from app.domain.entities.transpenetapan import TransPenetapan
from app.domain.repositories.transpenetapan_repository import TransPenetapanRepository
from app.infrastructure.orm.models import TransPenetapan as TransPenetapanModel


class TransPenetapanRepositoryImpl(TransPenetapanRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return (
            self.db.query(TransPenetapanModel)
            .order_by(TransPenetapanModel.idpenetapan.asc())
            .all()
        )

    def get_by_id(self, idpenetapan: int):
        return (
            self.db.query(TransPenetapanModel)
            .filter(TransPenetapanModel.idpenetapan == idpenetapan)
            .first()
        )

    def create(self, trans_penetapan: TransPenetapan):
        db_trans_penetapan = TransPenetapanModel(**trans_penetapan.__dict__)
        self.db.add(db_trans_penetapan)
        self.db.commit()
        self.db.refresh(db_trans_penetapan)
        return db_trans_penetapan

    def update(self, idpenetapan: int, trans_penetapan: TransPenetapan):
        db_trans_penetapan = self.get_by_id(idpenetapan)
        if not db_trans_penetapan:
            return None

        for key, value in trans_penetapan.__dict__.items():
            if key == "idpenetapan":
                continue
            if value is not None:
                setattr(db_trans_penetapan, key, value)

        self.db.commit()
        self.db.refresh(db_trans_penetapan)
        return db_trans_penetapan

    def delete(self, idpenetapan: int):
        db_trans_penetapan = self.get_by_id(idpenetapan)
        if not db_trans_penetapan:
            return False
        self.db.delete(db_trans_penetapan)
        self.db.commit()
        return True
