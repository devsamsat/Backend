from sqlalchemy.orm import Session

from app.domain.entities.jnsstrurek import JnsStruRek
from app.domain.repositories.jnsstrurek_repository import JnsStruRekRepository
from app.infrastructure.orm.models import JnsStruRek as JnsStruRekModel


class JnsStruRekRepositoryImpl(JnsStruRekRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(JnsStruRekModel).order_by(JnsStruRekModel.mtglevel.asc()).all()

    def get_by_id(self, mtglevel: str):
        return self.db.query(JnsStruRekModel).filter(JnsStruRekModel.mtglevel == mtglevel).first()

    def create(self, jns_strurek: JnsStruRek):
        db_record = JnsStruRekModel(**jns_strurek.__dict__)
        self.db.add(db_record)
        self.db.commit()
        self.db.refresh(db_record)
        return db_record

    def update(self, mtglevel: str, jns_strurek: JnsStruRek):
        db_record = self.get_by_id(mtglevel)
        if not db_record:
            return None

        for key, value in jns_strurek.__dict__.items():
            if key == "mtglevel":
                continue
            if value is not None:
                setattr(db_record, key, value)

        self.db.commit()
        self.db.refresh(db_record)
        return db_record

    def delete(self, mtglevel: str):
        db_record = self.get_by_id(mtglevel)
        if not db_record:
            return False
        self.db.delete(db_record)
        self.db.commit()
        return True
