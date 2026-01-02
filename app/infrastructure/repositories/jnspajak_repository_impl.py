from sqlalchemy.orm import Session

from app.domain.entities.jnspajak import JnsPajak
from app.domain.repositories.jnspajak_repository import JnsPajakRepository
from app.infrastructure.orm.models import JnsPajak as JnsPajakModel


class JnsPajakRepositoryImpl(JnsPajakRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(JnsPajakModel).order_by(JnsPajakModel.kdjnspjk.asc()).all()

    def get_by_id(self, kdjnspjk: str):
        return (
            self.db.query(JnsPajakModel)
            .filter(JnsPajakModel.kdjnspjk == kdjnspjk)
            .first()
        )

    def create(self, jns_pajak: JnsPajak):
        db_pajak = JnsPajakModel(**jns_pajak.__dict__)
        self.db.add(db_pajak)
        self.db.commit()
        self.db.refresh(db_pajak)
        return db_pajak

    def update(self, kdjnspjk: str, jns_pajak: JnsPajak):
        db_pajak = self.get_by_id(kdjnspjk)
        if not db_pajak:
            return None

        for key, value in jns_pajak.__dict__.items():
            if key == "kdjnspjk":
                continue
            if value is not None:
                setattr(db_pajak, key, value)

        self.db.commit()
        self.db.refresh(db_pajak)
        return db_pajak

    def delete(self, kdjnspjk: str):
        db_pajak = self.get_by_id(kdjnspjk)
        if not db_pajak:
            return False
        self.db.delete(db_pajak)
        self.db.commit()
        return True
