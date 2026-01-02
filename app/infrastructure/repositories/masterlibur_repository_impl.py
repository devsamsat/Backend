from sqlalchemy.orm import Session

from app.domain.entities.masterlibur import MasterLibur
from app.domain.repositories.masterlibur_repository import MasterLiburRepository
from app.infrastructure.orm.models import MasterLibur as MasterLiburModel


class MasterLiburRepositoryImpl(MasterLiburRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(MasterLiburModel).order_by(MasterLiburModel.idlibur.asc()).all()

    def get_by_id(self, idlibur: int):
        return self.db.query(MasterLiburModel).filter(MasterLiburModel.idlibur == idlibur).first()

    def create(self, master_libur: MasterLibur):
        db_record = MasterLiburModel(**master_libur.__dict__)
        self.db.add(db_record)
        self.db.commit()
        self.db.refresh(db_record)
        return db_record

    def update(self, idlibur: int, master_libur: MasterLibur):
        db_record = self.get_by_id(idlibur)
        if not db_record:
            return None

        for key, value in master_libur.__dict__.items():
            if key == "idlibur":
                continue
            if value is not None:
                setattr(db_record, key, value)

        self.db.commit()
        self.db.refresh(db_record)
        return db_record

    def delete(self, idlibur: int):
        db_record = self.get_by_id(idlibur)
        if not db_record:
            return False
        self.db.delete(db_record)
        self.db.commit()
        return True
