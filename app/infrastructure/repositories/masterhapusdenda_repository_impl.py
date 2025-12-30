from sqlalchemy.orm import Session

from app.domain.entities.masterhapusdenda import MasterHapusDenda
from app.domain.repositories.masterhapusdenda_repository import MasterHapusDendaRepository
from app.infrastructure.orm.models import MasterHapusDenda as MasterHapusDendaModel


class MasterHapusDendaRepositoryImpl(MasterHapusDendaRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(MasterHapusDendaModel).order_by(MasterHapusDendaModel.idhapusdenda.asc()).all()

    def get_by_id(self, idhapusdenda: int):
        return (
            self.db.query(MasterHapusDendaModel)
            .filter(MasterHapusDendaModel.idhapusdenda == idhapusdenda)
            .first()
        )

    def create(self, master_hapus_denda: MasterHapusDenda):
        db_master_hapus_denda = MasterHapusDendaModel(**master_hapus_denda.__dict__)
        self.db.add(db_master_hapus_denda)
        self.db.commit()
        self.db.refresh(db_master_hapus_denda)
        return db_master_hapus_denda

    def update(self, idhapusdenda: int, master_hapus_denda: MasterHapusDenda):
        db_master_hapus_denda = self.get_by_id(idhapusdenda)
        if not db_master_hapus_denda:
            return None

        for key, value in master_hapus_denda.__dict__.items():
            if key == "idhapusdenda":
                continue
            if value is not None:
                setattr(db_master_hapus_denda, key, value)

        self.db.commit()
        self.db.refresh(db_master_hapus_denda)
        return db_master_hapus_denda

    def delete(self, idhapusdenda: int):
        db_master_hapus_denda = self.get_by_id(idhapusdenda)
        if not db_master_hapus_denda:
            return False
        self.db.delete(db_master_hapus_denda)
        self.db.commit()
        return True
