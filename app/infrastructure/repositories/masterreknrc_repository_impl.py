from sqlalchemy.orm import Session

from app.domain.entities.masterreknrc import MasterRekNrc
from app.domain.repositories.masterreknrc_repository import MasterRekNrcRepository
from app.infrastructure.orm.models import MasterRekNrc as MasterRekNrcModel


class MasterRekNrcRepositoryImpl(MasterRekNrcRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return (
            self.db.query(MasterRekNrcModel)
            .order_by(MasterRekNrcModel.idreknrc.asc())
            .all()
        )

    def get_by_id(self, idreknrc: int):
        return (
            self.db.query(MasterRekNrcModel)
            .filter(MasterRekNrcModel.idreknrc == idreknrc)
            .first()
        )

    def create(self, master_reknrc: MasterRekNrc):
        db_master_reknrc = MasterRekNrcModel(**master_reknrc.__dict__)
        self.db.add(db_master_reknrc)
        self.db.commit()
        self.db.refresh(db_master_reknrc)
        return db_master_reknrc

    def update(self, idreknrc: int, master_reknrc: MasterRekNrc):
        db_master_reknrc = self.get_by_id(idreknrc)
        if not db_master_reknrc:
            return None

        for key, value in master_reknrc.__dict__.items():
            if key == "idreknrc":
                continue
            if value is not None:
                setattr(db_master_reknrc, key, value)

        self.db.commit()
        self.db.refresh(db_master_reknrc)
        return db_master_reknrc

    def delete(self, idreknrc: int):
        db_master_reknrc = self.get_by_id(idreknrc)
        if not db_master_reknrc:
            return False
        self.db.delete(db_master_reknrc)
        self.db.commit()
        return True
