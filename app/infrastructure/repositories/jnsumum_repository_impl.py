from sqlalchemy.orm import Session

from app.domain.entities.jnsumum import JnsUmum
from app.domain.repositories.jnsumum_repository import JnsUmumRepository
from app.infrastructure.orm.models import JnsUmum as JnsUmumModel


class JnsUmumRepositoryImpl(JnsUmumRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(JnsUmumModel).order_by(JnsUmumModel.kdumum.asc()).all()

    def get_by_id(self, kdumum: str):
        return self.db.query(JnsUmumModel).filter(JnsUmumModel.kdumum == kdumum).first()

    def create(self, jns_umum: JnsUmum):
        db_record = JnsUmumModel(**jns_umum.__dict__)
        self.db.add(db_record)
        self.db.commit()
        self.db.refresh(db_record)
        return db_record

    def update(self, kdumum: str, jns_umum: JnsUmum):
        db_record = self.get_by_id(kdumum)
        if not db_record:
            return None

        for key, value in jns_umum.__dict__.items():
            if key == "kdumum":
                continue
            if value is not None:
                setattr(db_record, key, value)

        self.db.commit()
        self.db.refresh(db_record)
        return db_record

    def delete(self, kdumum: str):
        db_record = self.get_by_id(kdumum)
        if not db_record:
            return False
        self.db.delete(db_record)
        self.db.commit()
        return True
