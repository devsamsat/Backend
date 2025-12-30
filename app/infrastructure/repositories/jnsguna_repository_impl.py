from sqlalchemy.orm import Session
from app.domain.entities.jnsguna import JnsGuna
from app.domain.repositories.jnsguna_repository import JnsGunaRepository
from app.infrastructure.orm.models import JnsGuna as JnsGunaModel


class JnsGunaRepositoryImpl(JnsGunaRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(JnsGunaModel).order_by(JnsGunaModel.kdguna.asc()).all()

    def get_by_id(self, kdguna: str):
        return self.db.query(JnsGunaModel).filter(JnsGunaModel.kdguna == kdguna).first()

    def create(self, jns_guna: JnsGuna):
        db_guna = JnsGunaModel(**jns_guna.__dict__)
        self.db.add(db_guna)
        self.db.commit()
        self.db.refresh(db_guna)
        return db_guna

    def update(self, kdguna: str, jns_guna: JnsGuna):
        db_guna = self.get_by_id(kdguna)
        if not db_guna:
            return None

        for key, value in jns_guna.__dict__.items():
            if key == "kdguna":
                continue
            if value is not None:
                setattr(db_guna, key, value)

        self.db.commit()
        self.db.refresh(db_guna)
        return db_guna

    def delete(self, kdguna: str):
        db_guna = self.get_by_id(kdguna)
        if not db_guna:
            return False
        self.db.delete(db_guna)
        self.db.commit()
        return True
