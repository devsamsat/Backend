from sqlalchemy.orm import Session

from app.domain.entities.masterkelurahan import MasterKelurahan
from app.domain.repositories.masterkelurahan_repository import MasterKelurahanRepository
from app.infrastructure.orm.models import MasterKelurahan as MasterKelurahanModel


class MasterKelurahanRepositoryImpl(MasterKelurahanRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return (
            self.db.query(MasterKelurahanModel)
            .order_by(MasterKelurahanModel.idkelurahan.asc())
            .all()
        )

    def get_by_id(self, idkelurahan: int):
        return (
            self.db.query(MasterKelurahanModel)
            .filter(MasterKelurahanModel.idkelurahan == idkelurahan)
            .first()
        )

    def create(self, master_kelurahan: MasterKelurahan):
        db_master_kelurahan = MasterKelurahanModel(**master_kelurahan.__dict__)
        self.db.add(db_master_kelurahan)
        self.db.commit()
        self.db.refresh(db_master_kelurahan)
        return db_master_kelurahan

    def update(self, idkelurahan: int, master_kelurahan: MasterKelurahan):
        db_master_kelurahan = self.get_by_id(idkelurahan)
        if not db_master_kelurahan:
            return None

        for key, value in master_kelurahan.__dict__.items():
            if key == "idkelurahan":
                continue
            if value is not None:
                setattr(db_master_kelurahan, key, value)

        self.db.commit()
        self.db.refresh(db_master_kelurahan)
        return db_master_kelurahan

    def delete(self, idkelurahan: int):
        db_master_kelurahan = self.get_by_id(idkelurahan)
        if not db_master_kelurahan:
            return False
        self.db.delete(db_master_kelurahan)
        self.db.commit()
        return True
