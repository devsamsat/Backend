from sqlalchemy.orm import Session

from app.domain.entities.masteruunjop import MasterUunJop
from app.domain.repositories.masteruunjop_repository import MasterUunJopRepository
from app.infrastructure.orm.models import MasterUunJop as MasterUunJopModel


class MasterUunJopRepositoryImpl(MasterUunJopRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return (
            self.db.query(MasterUunJopModel)
            .order_by(MasterUunJopModel.iduunjop.asc())
            .all()
        )

    def get_by_id(self, iduunjop: int):
        return (
            self.db.query(MasterUunJopModel)
            .filter(MasterUunJopModel.iduunjop == iduunjop)
            .first()
        )

    def create(self, master_uun_jop: MasterUunJop):
        db_master_uun_jop = MasterUunJopModel(**master_uun_jop.__dict__)
        self.db.add(db_master_uun_jop)
        self.db.commit()
        self.db.refresh(db_master_uun_jop)
        return db_master_uun_jop

    def update(self, iduunjop: int, master_uun_jop: MasterUunJop):
        db_master_uun_jop = self.get_by_id(iduunjop)
        if not db_master_uun_jop:
            return None

        for key, value in master_uun_jop.__dict__.items():
            if key == "iduunjop":
                continue
            if value is not None:
                setattr(db_master_uun_jop, key, value)

        self.db.commit()
        self.db.refresh(db_master_uun_jop)
        return db_master_uun_jop

    def delete(self, iduunjop: int):
        db_master_uun_jop = self.get_by_id(iduunjop)
        if not db_master_uun_jop:
            return False
        self.db.delete(db_master_uun_jop)
        self.db.commit()
        return True
