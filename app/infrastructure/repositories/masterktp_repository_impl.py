from sqlalchemy.orm import Session

from app.domain.entities.masterktp import MasterKtp
from app.domain.repositories.masterktp_repository import MasterKtpRepository
from app.infrastructure.orm.models import MasterKtp as MasterKtpModel


class MasterKtpRepositoryImpl(MasterKtpRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(MasterKtpModel).order_by(MasterKtpModel.idktp.asc()).all()

    def get_by_id(self, idktp: int):
        return self.db.query(MasterKtpModel).filter(MasterKtpModel.idktp == idktp).first()

    def create(self, master_ktp: MasterKtp):
        db_master_ktp = MasterKtpModel(**master_ktp.__dict__)
        self.db.add(db_master_ktp)
        self.db.commit()
        self.db.refresh(db_master_ktp)
        return db_master_ktp

    def update(self, idktp: int, master_ktp: MasterKtp):
        db_master_ktp = self.get_by_id(idktp)
        if not db_master_ktp:
            return None

        for key, value in master_ktp.__dict__.items():
            if key == "idktp":
                continue
            if value is not None:
                setattr(db_master_ktp, key, value)

        self.db.commit()
        self.db.refresh(db_master_ktp)
        return db_master_ktp

    def delete(self, idktp: int):
        db_master_ktp = self.get_by_id(idktp)
        if not db_master_ktp:
            return False
        self.db.delete(db_master_ktp)
        self.db.commit()
        return True
