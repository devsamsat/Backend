from sqlalchemy.orm import Session

from app.domain.entities.jnsmilik import JnsMilik
from app.domain.repositories.jnsmilik_repository import JnsMilikRepository
from app.infrastructure.orm.models import JnsMilik as JnsMilikModel


class JnsMilikRepositoryImpl(JnsMilikRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(JnsMilikModel).order_by(JnsMilikModel.kdmilik.asc()).all()

    def get_by_id(self, kdmilik: str):
        return self.db.query(JnsMilikModel).filter(JnsMilikModel.kdmilik == kdmilik).first()

    def create(self, jns_milik: JnsMilik):
        db_milik = JnsMilikModel(**jns_milik.__dict__)
        self.db.add(db_milik)
        self.db.commit()
        self.db.refresh(db_milik)
        return db_milik

    def update(self, kdmilik: str, jns_milik: JnsMilik):
        db_milik = self.get_by_id(kdmilik)
        if not db_milik:
            return None

        for key, value in jns_milik.__dict__.items():
            if key == "kdmilik":
                continue
            if value is not None:
                setattr(db_milik, key, value)

        self.db.commit()
        self.db.refresh(db_milik)
        return db_milik

    def delete(self, kdmilik: str):
        db_milik = self.get_by_id(kdmilik)
        if not db_milik:
            return False
        self.db.delete(db_milik)
        self.db.commit()
        return True
