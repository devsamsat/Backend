from sqlalchemy.orm import Session
from app.domain.entities.jnsgolongan import JnsGolongan
from app.domain.repositories.jnsgolongan_repository import JnsGolonganRepository
from app.infrastructure.orm.models import JnsGolongan as JnsGolonganModel


class JnsGolonganRepositoryImpl(JnsGolonganRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(JnsGolonganModel).order_by(JnsGolonganModel.jnsgolid.asc()).all()

    def get_by_id(self, jnsgolid: str):
        return self.db.query(JnsGolonganModel).filter(JnsGolonganModel.jnsgolid == jnsgolid).first()

    def create(self, jns_golongan: JnsGolongan):
        db_golongan = JnsGolonganModel(**jns_golongan.__dict__)
        self.db.add(db_golongan)
        self.db.commit()
        self.db.refresh(db_golongan)
        return db_golongan

    def update(self, jnsgolid: str, jns_golongan: JnsGolongan):
        db_golongan = self.get_by_id(jnsgolid)
        if not db_golongan:
            return None

        for key, value in jns_golongan.__dict__.items():
            if key == "jnsgolid":
                continue
            if value is not None:
                setattr(db_golongan, key, value)

        self.db.commit()
        self.db.refresh(db_golongan)
        return db_golongan

    def delete(self, jnsgolid: str):
        db_golongan = self.get_by_id(jnsgolid)
        if not db_golongan:
            return False
        self.db.delete(db_golongan)
        self.db.commit()
        return True
