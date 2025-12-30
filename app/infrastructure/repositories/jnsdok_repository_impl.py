from sqlalchemy.orm import Session
from app.domain.entities.jnsdok import JnsDok
from app.domain.repositories.jnsdok_repository import JnsDokRepository
from app.infrastructure.orm.models import JnsDokModel


class JnsDokRepositoryImpl(JnsDokRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(JnsDokModel).all()

    def get_by_id(self, kddok: str):
        return self.db.query(JnsDokModel).filter(JnsDokModel.kddok == kddok).first()

    def create(self, jnsdok: JnsDok):
        db_record = JnsDokModel(**jnsdok.__dict__)
        self.db.add(db_record)
        self.db.commit()
        self.db.refresh(db_record)
        return db_record

    def update(self, kddok: str, jnsdok: JnsDok):
        db_record = self.get_by_id(kddok)
        if not db_record:
            return None

        for key, value in jnsdok.__dict__.items():
            if value is not None and key != "kddok":
                setattr(db_record, key, value)

        self.db.commit()
        self.db.refresh(db_record)
        return db_record

    def delete(self, kddok: str):
        db_record = self.get_by_id(kddok)
        if not db_record:
            return False
        self.db.delete(db_record)
        self.db.commit()
        return True
