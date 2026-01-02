from sqlalchemy.orm import Session

from app.domain.entities.mastertarifnjop import MasterTarifNjop
from app.domain.repositories.mastertarifnjop_repository import MasterTarifNjopRepository
from app.infrastructure.orm.models import MasterTarifNjop as MasterTarifNjopModel


class MasterTarifNjopRepositoryImpl(MasterTarifNjopRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return (
            self.db.query(MasterTarifNjopModel)
            .order_by(MasterTarifNjopModel.idtarifnjop.asc())
            .all()
        )

    def get_by_id(self, idtarifnjop: int):
        return (
            self.db.query(MasterTarifNjopModel)
            .filter(MasterTarifNjopModel.idtarifnjop == idtarifnjop)
            .first()
        )

    def create(self, master_tarif_njop: MasterTarifNjop):
        db_master_tarif_njop = MasterTarifNjopModel(**master_tarif_njop.__dict__)
        self.db.add(db_master_tarif_njop)
        self.db.commit()
        self.db.refresh(db_master_tarif_njop)
        return db_master_tarif_njop

    def update(self, idtarifnjop: int, master_tarif_njop: MasterTarifNjop):
        db_master_tarif_njop = self.get_by_id(idtarifnjop)
        if not db_master_tarif_njop:
            return None

        for key, value in master_tarif_njop.__dict__.items():
            if key == "idtarifnjop":
                continue
            if value is not None:
                setattr(db_master_tarif_njop, key, value)

        self.db.commit()
        self.db.refresh(db_master_tarif_njop)
        return db_master_tarif_njop

    def delete(self, idtarifnjop: int):
        db_master_tarif_njop = self.get_by_id(idtarifnjop)
        if not db_master_tarif_njop:
            return False
        self.db.delete(db_master_tarif_njop)
        self.db.commit()
        return True
