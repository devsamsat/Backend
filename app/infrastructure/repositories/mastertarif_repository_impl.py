from sqlalchemy.orm import Session

from app.domain.entities.mastertarif import MasterTarif
from app.domain.repositories.mastertarif_repository import MasterTarifRepository
from app.infrastructure.orm.models import MasterTarif as MasterTarifModel


class MasterTarifRepositoryImpl(MasterTarifRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return (
            self.db.query(MasterTarifModel)
            .order_by(MasterTarifModel.idtarif.asc())
            .all()
        )

    def get_by_id(self, idtarif: int):
        return (
            self.db.query(MasterTarifModel)
            .filter(MasterTarifModel.idtarif == idtarif)
            .first()
        )

    def create(self, master_tarif: MasterTarif):
        db_master_tarif = MasterTarifModel(**master_tarif.__dict__)
        self.db.add(db_master_tarif)
        self.db.commit()
        self.db.refresh(db_master_tarif)
        return db_master_tarif

    def update(self, idtarif: int, master_tarif: MasterTarif):
        db_master_tarif = self.get_by_id(idtarif)
        if not db_master_tarif:
            return None

        for key, value in master_tarif.__dict__.items():
            if key == "idtarif":
                continue
            if value is not None:
                setattr(db_master_tarif, key, value)

        self.db.commit()
        self.db.refresh(db_master_tarif)
        return db_master_tarif

    def delete(self, idtarif: int):
        db_master_tarif = self.get_by_id(idtarif)
        if not db_master_tarif:
            return False
        self.db.delete(db_master_tarif)
        self.db.commit()
        return True
