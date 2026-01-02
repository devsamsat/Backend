from sqlalchemy.orm import Session

from app.domain.entities.masterkabkotaall import MasterKabKotaAll
from app.domain.repositories.masterkabkotaall_repository import (
    MasterKabKotaAllRepository,
)
from app.infrastructure.orm.models import MasterKabKotaAll as MasterKabKotaAllModel


class MasterKabKotaAllRepositoryImpl(MasterKabKotaAllRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return (
            self.db.query(MasterKabKotaAllModel)
            .order_by(MasterKabKotaAllModel.idkabkotaall.asc())
            .all()
        )

    def get_by_id(self, idkabkotaall: int):
        return (
            self.db.query(MasterKabKotaAllModel)
            .filter(MasterKabKotaAllModel.idkabkotaall == idkabkotaall)
            .first()
        )

    def create(self, master_kabkotaall: MasterKabKotaAll):
        db_master_kabkotaall = MasterKabKotaAllModel(**master_kabkotaall.__dict__)
        self.db.add(db_master_kabkotaall)
        self.db.commit()
        self.db.refresh(db_master_kabkotaall)
        return db_master_kabkotaall

    def update(self, idkabkotaall: int, master_kabkotaall: MasterKabKotaAll):
        db_master_kabkotaall = self.get_by_id(idkabkotaall)
        if not db_master_kabkotaall:
            return None

        for key, value in master_kabkotaall.__dict__.items():
            if key == "idkabkotaall":
                continue
            if value is not None:
                setattr(db_master_kabkotaall, key, value)

        self.db.commit()
        self.db.refresh(db_master_kabkotaall)
        return db_master_kabkotaall

    def delete(self, idkabkotaall: int):
        db_master_kabkotaall = self.get_by_id(idkabkotaall)
        if not db_master_kabkotaall:
            return False
        self.db.delete(db_master_kabkotaall)
        self.db.commit()
        return True
