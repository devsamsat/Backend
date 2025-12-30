from sqlalchemy.orm import Session

from app.domain.entities.masterhistory import MasterHistory
from app.domain.repositories.masterhistory_repository import MasterHistoryRepository
from app.infrastructure.orm.models import MasterHistory as MasterHistoryModel


class MasterHistoryRepositoryImpl(MasterHistoryRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(MasterHistoryModel).order_by(MasterHistoryModel.idhistory.asc()).all()

    def get_by_id(self, idhistory: int):
        return (
            self.db.query(MasterHistoryModel)
            .filter(MasterHistoryModel.idhistory == idhistory)
            .first()
        )

    def create(self, master_history: MasterHistory):
        db_master_history = MasterHistoryModel(**master_history.__dict__)
        self.db.add(db_master_history)
        self.db.commit()
        self.db.refresh(db_master_history)
        return db_master_history

    def update(self, idhistory: int, master_history: MasterHistory):
        db_master_history = self.get_by_id(idhistory)
        if not db_master_history:
            return None

        for key, value in master_history.__dict__.items():
            if key == "idhistory":
                continue
            if value is not None:
                setattr(db_master_history, key, value)

        self.db.commit()
        self.db.refresh(db_master_history)
        return db_master_history

    def delete(self, idhistory: int):
        db_master_history = self.get_by_id(idhistory)
        if not db_master_history:
            return False
        self.db.delete(db_master_history)
        self.db.commit()
        return True
