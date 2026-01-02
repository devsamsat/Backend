from sqlalchemy.orm import Session

from app.domain.entities.masterrt import MasterRt
from app.domain.repositories.masterrt_repository import MasterRtRepository
from app.infrastructure.orm.models import MasterRt as MasterRtModel


class MasterRtRepositoryImpl(MasterRtRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(MasterRtModel).order_by(MasterRtModel.idrt.asc()).all()

    def get_by_id(self, idrt: int):
        return self.db.query(MasterRtModel).filter(MasterRtModel.idrt == idrt).first()

    def create(self, master_rt: MasterRt):
        db_master_rt = MasterRtModel(**master_rt.__dict__)
        self.db.add(db_master_rt)
        self.db.commit()
        self.db.refresh(db_master_rt)
        return db_master_rt

    def update(self, idrt: int, master_rt: MasterRt):
        db_master_rt = self.get_by_id(idrt)
        if not db_master_rt:
            return None

        for key, value in master_rt.__dict__.items():
            if key == "idrt":
                continue
            if value is not None:
                setattr(db_master_rt, key, value)

        self.db.commit()
        self.db.refresh(db_master_rt)
        return db_master_rt

    def delete(self, idrt: int):
        db_master_rt = self.get_by_id(idrt)
        if not db_master_rt:
            return False
        self.db.delete(db_master_rt)
        self.db.commit()
        return True
