from sqlalchemy.orm import Session

from app.domain.entities.mastermerk import MasterMerk
from app.domain.repositories.mastermerk_repository import MasterMerkRepository
from app.infrastructure.orm.models import MasterMerk as MasterMerkModel


class MasterMerkRepositoryImpl(MasterMerkRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(MasterMerkModel).order_by(MasterMerkModel.idmerk.asc()).all()

    def get_by_id(self, idmerk: int):
        return self.db.query(MasterMerkModel).filter(MasterMerkModel.idmerk == idmerk).first()

    def create(self, master_merk: MasterMerk):
        db_record = MasterMerkModel(**master_merk.__dict__)
        self.db.add(db_record)
        self.db.commit()
        self.db.refresh(db_record)
        return db_record

    def update(self, idmerk: int, master_merk: MasterMerk):
        db_record = self.get_by_id(idmerk)
        if not db_record:
            return None

        for key, value in master_merk.__dict__.items():
            if key == "idmerk":
                continue
            if value is not None:
                setattr(db_record, key, value)

        self.db.commit()
        self.db.refresh(db_record)
        return db_record

    def delete(self, idmerk: int):
        db_record = self.get_by_id(idmerk)
        if not db_record:
            return False
        self.db.delete(db_record)
        self.db.commit()
        return True
