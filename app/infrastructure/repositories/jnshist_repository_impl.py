from sqlalchemy.orm import Session
from app.domain.entities.jnshist import JnsHist
from app.domain.repositories.jnshist_repository import JnsHistRepository
from app.infrastructure.orm.models import JnsHistModel


class JnsHistRepositoryImpl(JnsHistRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(JnsHistModel).all()

    def get_by_id(self, kdhist: str):
        return self.db.query(JnsHistModel).filter(JnsHistModel.kdhist == kdhist).first()

    def create(self, jnshist: JnsHist):
        db_record = JnsHistModel(**jnshist.__dict__)
        self.db.add(db_record)
        self.db.commit()
        self.db.refresh(db_record)
        return db_record

    def update(self, kdhist: str, jnshist: JnsHist):
        db_record = self.get_by_id(kdhist)
        if not db_record:
            return None

        for key, value in jnshist.__dict__.items():
            if value is not None and key != "kdhist":
                setattr(db_record, key, value)

        self.db.commit()
        self.db.refresh(db_record)
        return db_record

    def delete(self, kdhist: str):
        db_record = self.get_by_id(kdhist)
        if not db_record:
            return False
        self.db.delete(db_record)
        self.db.commit()
        return True
