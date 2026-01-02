from sqlalchemy.orm import Session

from app.domain.entities.jnskendaraan import JnsKendaraan
from app.domain.repositories.jnskendaraan_repository import JnsKendaraanRepository
from app.infrastructure.orm.models import JnsKendaraan as JnsKendaraanModel


class JnsKendaraanRepositoryImpl(JnsKendaraanRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return (
            self.db.query(JnsKendaraanModel)
            .order_by(JnsKendaraanModel.jnskendid.asc())
            .all()
        )

    def get_by_id(self, jnskendid: str):
        return (
            self.db.query(JnsKendaraanModel)
            .filter(JnsKendaraanModel.jnskendid == jnskendid)
            .first()
        )

    def create(self, jns_kendaraan: JnsKendaraan):
        db_kendaraan = JnsKendaraanModel(**jns_kendaraan.__dict__)
        self.db.add(db_kendaraan)
        self.db.commit()
        self.db.refresh(db_kendaraan)
        return db_kendaraan

    def update(self, jnskendid: str, jns_kendaraan: JnsKendaraan):
        db_kendaraan = self.get_by_id(jnskendid)
        if not db_kendaraan:
            return None

        for key, value in jns_kendaraan.__dict__.items():
            if key == "jnskendid":
                continue
            if value is not None:
                setattr(db_kendaraan, key, value)

        self.db.commit()
        self.db.refresh(db_kendaraan)
        return db_kendaraan

    def delete(self, jnskendid: str):
        db_kendaraan = self.get_by_id(jnskendid)
        if not db_kendaraan:
            return False
        self.db.delete(db_kendaraan)
        self.db.commit()
        return True
