from sqlalchemy.orm import Session
from app.domain.entities.jnsdok import JnsDok
from app.domain.repositories.jnsdok_repository import JnsDokRepository
from app.infrastructure.orm.models import JnsDok as JnsDokModel


class JnsDokRepositoryImpl(JnsDokRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(JnsDokModel).order_by(JnsDokModel.kddok.asc()).all()

    def get_by_id(self, kddok: str):
        return self.db.query(JnsDokModel).filter(JnsDokModel.kddok == kddok).first()

    def create(self, jns_dok: JnsDok):
        db_jns_dok = JnsDokModel(**jns_dok.__dict__)
        self.db.add(db_jns_dok)
        self.db.commit()
        self.db.refresh(db_jns_dok)
        return db_jns_dok

    def update(self, kddok: str, jns_dok: JnsDok):
        db_jns_dok = self.get_by_id(kddok)
        if not db_jns_dok:
            return None

        for key, value in jns_dok.__dict__.items():
            if key == "kddok":
                continue
            if value is not None:
                setattr(db_jns_dok, key, value)

        self.db.commit()
        self.db.refresh(db_jns_dok)
        return db_jns_dok

    def delete(self, kddok: str):
        db_jns_dok = self.get_by_id(kddok)
        if not db_jns_dok:
            return False
        self.db.delete(db_jns_dok)
        self.db.commit()
        return True
