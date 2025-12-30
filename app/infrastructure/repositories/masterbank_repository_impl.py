from sqlalchemy.orm import Session

from app.domain.entities.masterbank import MasterBank
from app.domain.repositories.masterbank_repository import MasterBankRepository
from app.infrastructure.orm.models import MasterBank as MasterBankModel


class MasterBankRepositoryImpl(MasterBankRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(MasterBankModel).order_by(MasterBankModel.idbank.asc()).all()

    def get_by_id(self, idbank: int):
        return self.db.query(MasterBankModel).filter(MasterBankModel.idbank == idbank).first()

    def create(self, master_bank: MasterBank):
        db_master_bank = MasterBankModel(**master_bank.__dict__)
        self.db.add(db_master_bank)
        self.db.commit()
        self.db.refresh(db_master_bank)
        return db_master_bank

    def update(self, idbank: int, master_bank: MasterBank):
        db_master_bank = self.get_by_id(idbank)
        if not db_master_bank:
            return None

        for key, value in master_bank.__dict__.items():
            if key == "idbank":
                continue
            if value is not None:
                setattr(db_master_bank, key, value)

        self.db.commit()
        self.db.refresh(db_master_bank)
        return db_master_bank

    def delete(self, idbank: int):
        db_master_bank = self.get_by_id(idbank)
        if not db_master_bank:
            return False
        self.db.delete(db_master_bank)
        self.db.commit()
        return True
