from sqlalchemy.orm import Session

from app.domain.entities.jnsjr import JnsJr
from app.domain.repositories.jnsjr_repository import JnsJrRepository
from app.infrastructure.orm.models import JnsJr as JnsJrModel


class JnsJrRepositoryImpl(JnsJrRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(JnsJrModel).order_by(JnsJrModel.jnsjrid.asc()).all()

    def get_by_id(self, jnsjrid: str):
        return self.db.query(JnsJrModel).filter(JnsJrModel.jnsjrid == jnsjrid).first()

    def create(self, jns_jr: JnsJr):
        db_jr = JnsJrModel(**jns_jr.__dict__)
        self.db.add(db_jr)
        self.db.commit()
        self.db.refresh(db_jr)
        return db_jr

    def update(self, jnsjrid: str, jns_jr: JnsJr):
        db_jr = self.get_by_id(jnsjrid)
        if not db_jr:
            return None

        for key, value in jns_jr.__dict__.items():
            if key == "jnsjrid":
                continue
            if value is not None:
                setattr(db_jr, key, value)

        self.db.commit()
        self.db.refresh(db_jr)
        return db_jr

    def delete(self, jnsjrid: str):
        db_jr = self.get_by_id(jnsjrid)
        if not db_jr:
            return False
        self.db.delete(db_jr)
        self.db.commit()
        return True
