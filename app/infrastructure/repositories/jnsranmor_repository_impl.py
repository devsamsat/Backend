from sqlalchemy.orm import Session

from app.domain.entities.jnsranmor import JnsRanmor
from app.domain.repositories.jnsranmor_repository import JnsRanmorRepository
from app.infrastructure.orm.models import JnsRanmor as JnsRanmorModel


class JnsRanmorRepositoryImpl(JnsRanmorRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(JnsRanmorModel).order_by(JnsRanmorModel.kdranmor.asc()).all()

    def get_by_id(self, kdranmor: str):
        return (
            self.db.query(JnsRanmorModel)
            .filter(JnsRanmorModel.kdranmor == kdranmor)
            .first()
        )

    def create(self, jns_ranmor: JnsRanmor):
        db_ranmor = JnsRanmorModel(**jns_ranmor.__dict__)
        self.db.add(db_ranmor)
        self.db.commit()
        self.db.refresh(db_ranmor)
        return db_ranmor

    def update(self, kdranmor: str, jns_ranmor: JnsRanmor):
        db_ranmor = self.get_by_id(kdranmor)
        if not db_ranmor:
            return None

        for key, value in jns_ranmor.__dict__.items():
            if key == "kdranmor":
                continue
            if value is not None:
                setattr(db_ranmor, key, value)

        self.db.commit()
        self.db.refresh(db_ranmor)
        return db_ranmor

    def delete(self, kdranmor: str):
        db_ranmor = self.get_by_id(kdranmor)
        if not db_ranmor:
            return False
        self.db.delete(db_ranmor)
        self.db.commit()
        return True
