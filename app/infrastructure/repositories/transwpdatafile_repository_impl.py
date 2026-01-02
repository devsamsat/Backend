from sqlalchemy.orm import Session

from app.domain.entities.transwpdatafile import TransWpDataFile
from app.domain.repositories.transwpdatafile_repository import TransWpDataFileRepository
from app.infrastructure.orm.models import TransWpDataFile as TransWpDataFileModel


class TransWpDataFileRepositoryImpl(TransWpDataFileRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return (
            self.db.query(TransWpDataFileModel)
            .order_by(TransWpDataFileModel.idfile.asc())
            .all()
        )

    def get_by_id(self, idfile: int):
        return (
            self.db.query(TransWpDataFileModel)
            .filter(TransWpDataFileModel.idfile == idfile)
            .first()
        )

    def create(self, trans_wpdatafile: TransWpDataFile):
        db_trans_wpdatafile = TransWpDataFileModel(**trans_wpdatafile.__dict__)
        self.db.add(db_trans_wpdatafile)
        self.db.commit()
        self.db.refresh(db_trans_wpdatafile)
        return db_trans_wpdatafile

    def update(self, idfile: int, trans_wpdatafile: TransWpDataFile):
        db_trans_wpdatafile = self.get_by_id(idfile)
        if not db_trans_wpdatafile:
            return None

        for key, value in trans_wpdatafile.__dict__.items():
            if key == "idfile":
                continue
            if value is not None:
                setattr(db_trans_wpdatafile, key, value)

        self.db.commit()
        self.db.refresh(db_trans_wpdatafile)
        return db_trans_wpdatafile

    def delete(self, idfile: int):
        db_trans_wpdatafile = self.get_by_id(idfile)
        if not db_trans_wpdatafile:
            return False
        self.db.delete(db_trans_wpdatafile)
        self.db.commit()
        return True
