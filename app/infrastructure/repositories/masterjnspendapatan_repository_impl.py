from sqlalchemy.orm import Session

from app.domain.entities.masterjnspendapatan import MasterJnsPendapatan
from app.domain.repositories.masterjnspendapatan_repository import (
    MasterJnsPendapatanRepository,
)
from app.infrastructure.orm.models import MasterJnsPendapatan as MasterJnsPendapatanModel


class MasterJnsPendapatanRepositoryImpl(MasterJnsPendapatanRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return (
            self.db.query(MasterJnsPendapatanModel)
            .order_by(MasterJnsPendapatanModel.idjnsd.asc())
            .all()
        )

    def get_by_id(self, idjnsd: int):
        return (
            self.db.query(MasterJnsPendapatanModel)
            .filter(MasterJnsPendapatanModel.idjnsd == idjnsd)
            .first()
        )

    def create(self, master_jns_pendapatan: MasterJnsPendapatan):
        db_master_jns_pendapatan = MasterJnsPendapatanModel(**master_jns_pendapatan.__dict__)
        self.db.add(db_master_jns_pendapatan)
        self.db.commit()
        self.db.refresh(db_master_jns_pendapatan)
        return db_master_jns_pendapatan

    def update(self, idjnsd: int, master_jns_pendapatan: MasterJnsPendapatan):
        db_master_jns_pendapatan = self.get_by_id(idjnsd)
        if not db_master_jns_pendapatan:
            return None

        for key, value in master_jns_pendapatan.__dict__.items():
            if key == "idjnsd":
                continue
            if value is not None:
                setattr(db_master_jns_pendapatan, key, value)

        self.db.commit()
        self.db.refresh(db_master_jns_pendapatan)
        return db_master_jns_pendapatan

    def delete(self, idjnsd: int):
        db_master_jns_pendapatan = self.get_by_id(idjnsd)
        if not db_master_jns_pendapatan:
            return False
        self.db.delete(db_master_jns_pendapatan)
        self.db.commit()
        return True
