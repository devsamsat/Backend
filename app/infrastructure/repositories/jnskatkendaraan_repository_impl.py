from sqlalchemy.orm import Session

from app.domain.entities.jnskatkendaraan import JnsKatKendaraan
from app.domain.repositories.jnskatkendaraan_repository import JnsKatKendaraanRepository
from app.infrastructure.orm.models import JnsKatKendaraan as JnsKatKendaraanModel


class JnsKatKendaraanRepositoryImpl(JnsKatKendaraanRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return (
            self.db.query(JnsKatKendaraanModel)
            .order_by(JnsKatKendaraanModel.katid.asc())
            .all()
        )

    def get_by_id(self, katid: str):
        return (
            self.db.query(JnsKatKendaraanModel)
            .filter(JnsKatKendaraanModel.katid == katid)
            .first()
        )

    def create(self, jns_katkendaraan: JnsKatKendaraan):
        db_katkendaraan = JnsKatKendaraanModel(**jns_katkendaraan.__dict__)
        self.db.add(db_katkendaraan)
        self.db.commit()
        self.db.refresh(db_katkendaraan)
        return db_katkendaraan

    def update(self, katid: str, jns_katkendaraan: JnsKatKendaraan):
        db_katkendaraan = self.get_by_id(katid)
        if not db_katkendaraan:
            return None

        for key, value in jns_katkendaraan.__dict__.items():
            if key == "katid":
                continue
            if value is not None:
                setattr(db_katkendaraan, key, value)

        self.db.commit()
        self.db.refresh(db_katkendaraan)
        return db_katkendaraan

    def delete(self, katid: str):
        db_katkendaraan = self.get_by_id(katid)
        if not db_katkendaraan:
            return False
        self.db.delete(db_katkendaraan)
        self.db.commit()
        return True
