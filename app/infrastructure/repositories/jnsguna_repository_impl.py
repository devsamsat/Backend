from sqlalchemy.orm import Session
from app.domain.entities.jnsguna import JnsGuna
from app.domain.repositories.jnsguna_repository import JnsGunaRepository
from app.infrastructure.orm.models import JnsGunaModel


class JnsGunaRepositoryImpl(JnsGunaRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(JnsGunaModel).all()

    def get_by_id(self, kdguna: str):
        return self.db.query(JnsGunaModel).filter(JnsGunaModel.kdguna == kdguna).first()

    def create(self, jnsguna: JnsGuna):
        db_record = JnsGunaModel(**jnsguna.__dict__)
        self.db.add(db_record)
        self.db.commit()
        self.db.refresh(db_record)
        return db_record

    def update(self, kdguna: str, jnsguna: JnsGuna):
        db_record = self.get_by_id(kdguna)
        if not db_record:
            return None

        for key, value in jnsguna.__dict__.items():
            if value is not None and key != "kdguna":
                setattr(db_record, key, value)

        self.db.commit()
        self.db.refresh(db_record)
        return db_record

    def delete(self, kdguna: str):
        db_record = self.get_by_id(kdguna)
        if not db_record:
            return False
        self.db.delete(db_record)
        self.db.commit()
        return True
