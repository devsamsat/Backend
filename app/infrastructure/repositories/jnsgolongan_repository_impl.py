from sqlalchemy.orm import Session
from app.domain.entities.jnsgolongan import JnsGolongan
from app.domain.repositories.jnsgolongan_repository import JnsGolonganRepository
from app.infrastructure.orm.models import JnsGolonganModel


class JnsGolonganRepositoryImpl(JnsGolonganRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(JnsGolonganModel).all()

    def get_by_id(self, jnsgolid: str):
        return (
            self.db.query(JnsGolonganModel)
            .filter(JnsGolonganModel.jnsgolid == jnsgolid)
            .first()
        )

    def create(self, jnsgolongan: JnsGolongan):
        db_record = JnsGolonganModel(**jnsgolongan.__dict__)
        self.db.add(db_record)
        self.db.commit()
        self.db.refresh(db_record)
        return db_record

    def update(self, jnsgolid: str, jnsgolongan: JnsGolongan):
        db_record = self.get_by_id(jnsgolid)
        if not db_record:
            return None

        for key, value in jnsgolongan.__dict__.items():
            if value is not None and key != "jnsgolid":
                setattr(db_record, key, value)

        self.db.commit()
        self.db.refresh(db_record)
        return db_record

    def delete(self, jnsgolid: str):
        db_record = self.get_by_id(jnsgolid)
        if not db_record:
            return False
        self.db.delete(db_record)
        self.db.commit()
        return True
