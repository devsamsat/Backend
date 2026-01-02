from sqlalchemy.orm import Session

from app.domain.entities.jnsplat import JnsPlat
from app.domain.repositories.jnsplat_repository import JnsPlatRepository
from app.infrastructure.orm.models import JnsPlat as JnsPlatModel


class JnsPlatRepositoryImpl(JnsPlatRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(JnsPlatModel).order_by(JnsPlatModel.kdplat.asc()).all()

    def get_by_id(self, kdplat: str):
        return self.db.query(JnsPlatModel).filter(JnsPlatModel.kdplat == kdplat).first()

    def create(self, jns_plat: JnsPlat):
        db_plat = JnsPlatModel(**jns_plat.__dict__)
        self.db.add(db_plat)
        self.db.commit()
        self.db.refresh(db_plat)
        return db_plat

    def update(self, kdplat: str, jns_plat: JnsPlat):
        db_plat = self.get_by_id(kdplat)
        if not db_plat:
            return None

        for key, value in jns_plat.__dict__.items():
            if key == "kdplat":
                continue
            if value is not None:
                setattr(db_plat, key, value)

        self.db.commit()
        self.db.refresh(db_plat)
        return db_plat

    def delete(self, kdplat: str):
        db_plat = self.get_by_id(kdplat)
        if not db_plat:
            return False
        self.db.delete(db_plat)
        self.db.commit()
        return True
