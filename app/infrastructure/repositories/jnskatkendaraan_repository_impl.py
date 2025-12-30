from sqlalchemy.orm import Session
from app.domain.entities.jnskatkendaraan import JnsKatKendaraan
from app.domain.repositories.jnskatkendaraan_repository import JnsKatKendaraanRepository
from app.infrastructure.orm.models import JnsKatKendaraanModel


class JnsKatKendaraanRepositoryImpl(JnsKatKendaraanRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(JnsKatKendaraanModel).all()

    def get_by_id(self, katid: str):
        return (
            self.db.query(JnsKatKendaraanModel)
            .filter(JnsKatKendaraanModel.katid == katid)
            .first()
        )

    def create(self, jnskatkendaraan: JnsKatKendaraan):
        db_record = JnsKatKendaraanModel(**jnskatkendaraan.__dict__)
        self.db.add(db_record)
        self.db.commit()
        self.db.refresh(db_record)
        return db_record

    def update(self, katid: str, jnskatkendaraan: JnsKatKendaraan):
        db_record = self.get_by_id(katid)
        if not db_record:
            return None

        for key, value in jnskatkendaraan.__dict__.items():
            if value is not None and key != "katid":
                setattr(db_record, key, value)

        self.db.commit()
        self.db.refresh(db_record)
        return db_record

    def delete(self, katid: str):
        db_record = self.get_by_id(katid)
        if not db_record:
            return False
        self.db.delete(db_record)
        self.db.commit()
        return True
