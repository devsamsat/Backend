from sqlalchemy.orm import Session

from app.domain.entities.jnsprogresif import JnsProgresif
from app.domain.repositories.jnsprogresif_repository import JnsProgresifRepository
from app.infrastructure.orm.models import JnsProgresif as JnsProgresifModel


class JnsProgresifRepositoryImpl(JnsProgresifRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return (
            self.db.query(JnsProgresifModel)
            .order_by(JnsProgresifModel.kdprogresif.asc())
            .all()
        )

    def get_by_id(self, kdprogresif: int):
        return (
            self.db.query(JnsProgresifModel)
            .filter(JnsProgresifModel.kdprogresif == kdprogresif)
            .first()
        )

    def create(self, jns_progresif: JnsProgresif):
        db_progresif = JnsProgresifModel(**jns_progresif.__dict__)
        self.db.add(db_progresif)
        self.db.commit()
        self.db.refresh(db_progresif)
        return db_progresif

    def update(self, kdprogresif: int, jns_progresif: JnsProgresif):
        db_progresif = self.get_by_id(kdprogresif)
        if not db_progresif:
            return None

        for key, value in jns_progresif.__dict__.items():
            if key == "kdprogresif":
                continue
            if value is not None:
                setattr(db_progresif, key, value)

        self.db.commit()
        self.db.refresh(db_progresif)
        return db_progresif

    def delete(self, kdprogresif: int):
        db_progresif = self.get_by_id(kdprogresif)
        if not db_progresif:
            return False
        self.db.delete(db_progresif)
        self.db.commit()
        return True
