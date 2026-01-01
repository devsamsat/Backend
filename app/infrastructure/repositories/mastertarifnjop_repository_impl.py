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

    def create(self, tarif: MasterTarifNjop):
        db_tarif = MasterTarifNjopModel(**tarif.__dict__)
        self.db.add(db_tarif)
        self.db.commit()
        self.db.refresh(db_tarif)
        return db_tarif

    def update(self, idtarifnjop: int, tarif: MasterTarifNjop):
        db_tarif = self.get_by_id(idtarifnjop)
        if not db_tarif:
            return None

        for key, value in tarif.__dict__.items():
            if key == "idtarifnjop":
                continue
            if value is not None:
                setattr(db_tarif, key, value)

        self.db.commit()
        self.db.refresh(db_tarif)
        return db_tarif

    def delete(self, idtarifnjop: int):
        db_tarif = self.get_by_id(idtarifnjop)
        if not db_tarif:
            return False
        self.db.delete(db_tarif)
        self.db.commit()
        return True
