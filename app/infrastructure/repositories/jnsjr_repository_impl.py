from sqlalchemy.orm import Session
from app.domain.entities.jnsjr import JnsJr
from app.domain.repositories.jnsjr_repository import JnsJrRepository
from app.infrastructure.orm.models import JnsJrModel


class JnsJrRepositoryImpl(JnsJrRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(JnsJrModel).all()

    def get_by_id(self, jnsjrid: str):
        return self.db.query(JnsJrModel).filter(JnsJrModel.jnsjrid == jnsjrid).first()

    def create(self, jnsjr: JnsJr):
        db_record = JnsJrModel(**jnsjr.__dict__)
        self.db.add(db_record)
        self.db.commit()
        self.db.refresh(db_record)
        return db_record

    def update(self, jnsjrid: str, jnsjr: JnsJr):
        db_record = self.get_by_id(jnsjrid)
        if not db_record:
            return None

        for key, value in jnsjr.__dict__.items():
            if value is not None and key != "jnsjrid":
                setattr(db_record, key, value)

        self.db.commit()
        self.db.refresh(db_record)
        return db_record

    def delete(self, jnsjrid: str):
        db_record = self.get_by_id(jnsjrid)
        if not db_record:
            return False
        self.db.delete(db_record)
        self.db.commit()
        return True
