from sqlalchemy.orm import Session

from app.domain.entities.transsts import TransSts
from app.domain.repositories.transsts_repository import TransStsRepository
from app.infrastructure.orm.models import TransSts as TransStsModel


class TransStsRepositoryImpl(TransStsRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(TransStsModel).order_by(TransStsModel.idsts.asc()).all()

    def get_by_id(self, idsts: int):
        return self.db.query(TransStsModel).filter(TransStsModel.idsts == idsts).first()

    def create(self, trans_sts: TransSts):
        db_trans_sts = TransStsModel(**trans_sts.__dict__)
        self.db.add(db_trans_sts)
        self.db.commit()
        self.db.refresh(db_trans_sts)
        return db_trans_sts

    def update(self, idsts: int, trans_sts: TransSts):
        db_trans_sts = self.get_by_id(idsts)
        if not db_trans_sts:
            return None

        for key, value in trans_sts.__dict__.items():
            if key == "idsts":
                continue
            if value is not None:
                setattr(db_trans_sts, key, value)

        self.db.commit()
        self.db.refresh(db_trans_sts)
        return db_trans_sts

    def delete(self, idsts: int):
        db_trans_sts = self.get_by_id(idsts)
        if not db_trans_sts:
            return False
        self.db.delete(db_trans_sts)
        self.db.commit()
        return True
