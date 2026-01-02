from sqlalchemy.orm import Session

from app.domain.entities.masterkabkota import MasterKabKota
from app.domain.repositories.masterkabkota_repository import MasterKabKotaRepository
from app.infrastructure.orm.models import MasterKabKota as MasterKabKotaModel


class MasterKabKotaRepositoryImpl(MasterKabKotaRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return (
            self.db.query(MasterKabKotaModel)
            .order_by(MasterKabKotaModel.idkabkota.asc())
            .all()
        )

    def get_by_id(self, idkabkota: int):
        return (
            self.db.query(MasterKabKotaModel)
            .filter(MasterKabKotaModel.idkabkota == idkabkota)
            .first()
        )

    def create(self, master_kabkota: MasterKabKota):
        db_master_kabkota = MasterKabKotaModel(**master_kabkota.__dict__)
        self.db.add(db_master_kabkota)
        self.db.commit()
        self.db.refresh(db_master_kabkota)
        return db_master_kabkota

    def update(self, idkabkota: int, master_kabkota: MasterKabKota):
        db_master_kabkota = self.get_by_id(idkabkota)
        if not db_master_kabkota:
            return None

        for key, value in master_kabkota.__dict__.items():
            if key == "idkabkota":
                continue
            if value is not None:
                setattr(db_master_kabkota, key, value)

        self.db.commit()
        self.db.refresh(db_master_kabkota)
        return db_master_kabkota

    def delete(self, idkabkota: int):
        db_master_kabkota = self.get_by_id(idkabkota)
        if not db_master_kabkota:
            return False
        self.db.delete(db_master_kabkota)
        self.db.commit()
        return True
