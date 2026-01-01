from sqlalchemy.orm import Session
from app.domain.entities.masterteks import MasterTeks
from app.domain.repositories.masterteks_repository import MasterTeksRepository
from app.infrastructure.orm.models import MasterTeks as MasterTeksModel


class MasterTeksRepositoryImpl(MasterTeksRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(MasterTeksModel).order_by(MasterTeksModel.idteks.asc()).all()

    def get_by_id(self, idteks: int):
        return self.db.query(MasterTeksModel).filter(MasterTeksModel.idteks == idteks).first()

    def create(self, teks: MasterTeks):
        db_teks = MasterTeksModel(**teks.__dict__)
        self.db.add(db_teks)
        self.db.commit()
        self.db.refresh(db_teks)
        return db_teks

    def update(self, idteks: int, teks: MasterTeks):
        db_teks = self.get_by_id(idteks)
        if not db_teks:
            return None

        for key, value in teks.__dict__.items():
            if key == "idteks":
                continue
            if value is not None:
                setattr(db_teks, key, value)

        self.db.commit()
        self.db.refresh(db_teks)
        return db_teks

    def delete(self, idteks: int):
        db_teks = self.get_by_id(idteks)
        if not db_teks:
            return False
        self.db.delete(db_teks)
        self.db.commit()
        return True
