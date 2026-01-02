from sqlalchemy.orm import Session

from app.domain.entities.jnstarif import JnsTarif
from app.domain.repositories.jnstarif_repository import JnsTarifRepository
from app.infrastructure.orm.models import JnsTarif as JnsTarifModel


class JnsTarifRepositoryImpl(JnsTarifRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(JnsTarifModel).order_by(JnsTarifModel.kdjnstarif.asc()).all()

    def get_by_id(self, kdjnstarif: str):
        return (
            self.db.query(JnsTarifModel)
            .filter(JnsTarifModel.kdjnstarif == kdjnstarif)
            .first()
        )

    def create(self, jns_tarif: JnsTarif):
        db_record = JnsTarifModel(**jns_tarif.__dict__)
        self.db.add(db_record)
        self.db.commit()
        self.db.refresh(db_record)
        return db_record

    def update(self, kdjnstarif: str, jns_tarif: JnsTarif):
        db_record = self.get_by_id(kdjnstarif)
        if not db_record:
            return None

        for key, value in jns_tarif.__dict__.items():
            if key == "kdjnstarif":
                continue
            if value is not None:
                setattr(db_record, key, value)

        self.db.commit()
        self.db.refresh(db_record)
        return db_record

    def delete(self, kdjnstarif: str):
        db_record = self.get_by_id(kdjnstarif)
        if not db_record:
            return False
        self.db.delete(db_record)
        self.db.commit()
        return True
