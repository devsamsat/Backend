from sqlalchemy.orm import Session

from app.domain.entities.masterabdet import MasterAbDet
from app.domain.repositories.masterabdet_repository import MasterAbDetRepository
from app.infrastructure.orm.models import MasterAbDet as MasterAbDetModel


class MasterAbDetRepositoryImpl(MasterAbDetRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(MasterAbDetModel).order_by(MasterAbDetModel.idabdet.asc()).all()

    def get_by_id(self, idabdet: int):
        return self.db.query(MasterAbDetModel).filter(MasterAbDetModel.idabdet == idabdet).first()

    def create(self, master_ab_det: MasterAbDet):
        db_master_ab_det = MasterAbDetModel(**master_ab_det.__dict__)
        self.db.add(db_master_ab_det)
        self.db.commit()
        self.db.refresh(db_master_ab_det)
        return db_master_ab_det

    def update(self, idabdet: int, master_ab_det: MasterAbDet):
        db_master_ab_det = self.get_by_id(idabdet)
        if not db_master_ab_det:
            return None

        for key, value in master_ab_det.__dict__.items():
            if key == "idabdet":
                continue
            if value is not None:
                setattr(db_master_ab_det, key, value)

        self.db.commit()
        self.db.refresh(db_master_ab_det)
        return db_master_ab_det

    def delete(self, idabdet: int):
        db_master_ab_det = self.get_by_id(idabdet)
        if not db_master_ab_det:
            return False
        self.db.delete(db_master_ab_det)
        self.db.commit()
        return True
