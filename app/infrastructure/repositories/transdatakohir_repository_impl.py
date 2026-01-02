from sqlalchemy.orm import Session

from app.domain.entities.transdatakohir import TransDataKohir
from app.domain.repositories.transdatakohir_repository import TransDataKohirRepository
from app.infrastructure.orm.models import TransDataKohir as TransDataKohirModel


class TransDataKohirRepositoryImpl(TransDataKohirRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return (
            self.db.query(TransDataKohirModel)
            .order_by(TransDataKohirModel.idkohir.asc())
            .all()
        )

    def get_by_id(self, idkohir: int):
        return (
            self.db.query(TransDataKohirModel)
            .filter(TransDataKohirModel.idkohir == idkohir)
            .first()
        )

    def create(self, trans_data_kohir: TransDataKohir):
        db_trans_data_kohir = TransDataKohirModel(**trans_data_kohir.__dict__)
        self.db.add(db_trans_data_kohir)
        self.db.commit()
        self.db.refresh(db_trans_data_kohir)
        return db_trans_data_kohir

    def update(self, idkohir: int, trans_data_kohir: TransDataKohir):
        db_trans_data_kohir = self.get_by_id(idkohir)
        if not db_trans_data_kohir:
            return None

        for key, value in trans_data_kohir.__dict__.items():
            if key == "idkohir":
                continue
            if value is not None:
                setattr(db_trans_data_kohir, key, value)

        self.db.commit()
        self.db.refresh(db_trans_data_kohir)
        return db_trans_data_kohir

    def delete(self, idkohir: int):
        db_trans_data_kohir = self.get_by_id(idkohir)
        if not db_trans_data_kohir:
            return False
        self.db.delete(db_trans_data_kohir)
        self.db.commit()
        return True
