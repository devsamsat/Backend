from sqlalchemy.orm import Session

from app.domain.entities.jnshist import JnsHist
from app.domain.repositories.jnshist_repository import JnsHistRepository
from app.infrastructure.orm.models import JnsHist as JnsHistModel


class JnsHistRepositoryImpl(JnsHistRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(JnsHistModel).order_by(JnsHistModel.kdhist.asc()).all()

    def get_by_id(self, kdhist: str):
        return self.db.query(JnsHistModel).filter(JnsHistModel.kdhist == kdhist).first()

    def create(self, jns_hist: JnsHist):
        db_hist = JnsHistModel(**jns_hist.__dict__)
        self.db.add(db_hist)
        self.db.commit()
        self.db.refresh(db_hist)
        return db_hist

    def update(self, kdhist: str, jns_hist: JnsHist):
        db_hist = self.get_by_id(kdhist)
        if not db_hist:
            return None

        for key, value in jns_hist.__dict__.items():
            if key == "kdhist":
                continue
            if value is not None:
                setattr(db_hist, key, value)

        self.db.commit()
        self.db.refresh(db_hist)
        return db_hist

    def delete(self, kdhist: str):
        db_hist = self.get_by_id(kdhist)
        if not db_hist:
            return False
        self.db.delete(db_hist)
        self.db.commit()
        return True
