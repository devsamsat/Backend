from sqlalchemy.orm import Session

from app.domain.entities.masterflow import MasterFlow
from app.domain.repositories.masterflow_repository import MasterFlowRepository
from app.infrastructure.orm.models import MasterFlow as MasterFlowModel


class MasterFlowRepositoryImpl(MasterFlowRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(MasterFlowModel).order_by(MasterFlowModel.kdflow.asc()).all()

    def get_by_id(self, kdflow: str):
        return self.db.query(MasterFlowModel).filter(MasterFlowModel.kdflow == kdflow).first()

    def create(self, master_flow: MasterFlow):
        db_master_flow = MasterFlowModel(**master_flow.__dict__)
        self.db.add(db_master_flow)
        self.db.commit()
        self.db.refresh(db_master_flow)
        return db_master_flow

    def update(self, kdflow: str, master_flow: MasterFlow):
        db_master_flow = self.get_by_id(kdflow)
        if not db_master_flow:
            return None

        for key, value in master_flow.__dict__.items():
            if key == "kdflow":
                continue
            if value is not None:
                setattr(db_master_flow, key, value)

        self.db.commit()
        self.db.refresh(db_master_flow)
        return db_master_flow

    def delete(self, kdflow: str):
        db_master_flow = self.get_by_id(kdflow)
        if not db_master_flow:
            return False
        self.db.delete(db_master_flow)
        self.db.commit()
        return True
