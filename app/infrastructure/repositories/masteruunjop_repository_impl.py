from sqlalchemy.orm import Session
from app.domain.entities.masteruunjop import MasterUuNjop
from app.domain.repositories.masteruunjop_repository import MasterUuNjopRepository
from app.infrastructure.orm.models import MasterUuNjop as MasterUuNjopModel


class MasterUuNjopRepositoryImpl(MasterUuNjopRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return (
            self.db.query(MasterUuNjopModel)
            .order_by(MasterUuNjopModel.iduunjop.asc())
            .all()
        )

    def get_by_id(self, iduunjop: int):
        return (
            self.db.query(MasterUuNjopModel)
            .filter(MasterUuNjopModel.iduunjop == iduunjop)
            .first()
        )

    def create(self, uu_njop: MasterUuNjop):
        db_uunjop = MasterUuNjopModel(**uu_njop.__dict__)
        self.db.add(db_uunjop)
        self.db.commit()
        self.db.refresh(db_uunjop)
        return db_uunjop

    def update(self, iduunjop: int, uu_njop: MasterUuNjop):
        db_uunjop = self.get_by_id(iduunjop)
        if not db_uunjop:
            return None

        for key, value in uu_njop.__dict__.items():
            if key == "iduunjop":
                continue
            if value is not None:
                setattr(db_uunjop, key, value)

        self.db.commit()
        self.db.refresh(db_uunjop)
        return db_uunjop

    def delete(self, iduunjop: int):
        db_uunjop = self.get_by_id(iduunjop)
        if not db_uunjop:
            return False
        self.db.delete(db_uunjop)
        self.db.commit()
        return True
