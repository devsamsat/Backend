from sqlalchemy.orm import Session

from app.domain.entities.mapjnspendapatan import MapJnsPendapatan
from app.domain.repositories.mapjnspendapatan_repository import MapJnsPendapatanRepository
from app.infrastructure.orm.models import MapJnsPendapatan as MapJnsPendapatanModel


class MapJnsPendapatanRepositoryImpl(MapJnsPendapatanRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return (
            self.db.query(MapJnsPendapatanModel)
            .order_by(MapJnsPendapatanModel.idmapjnsd.asc())
            .all()
        )

    def get_by_id(self, idmapjnsd: int):
        return (
            self.db.query(MapJnsPendapatanModel)
            .filter(MapJnsPendapatanModel.idmapjnsd == idmapjnsd)
            .first()
        )

    def create(self, map_jns_pendapatan: MapJnsPendapatan):
        db_record = MapJnsPendapatanModel(**map_jns_pendapatan.__dict__)
        self.db.add(db_record)
        self.db.commit()
        self.db.refresh(db_record)
        return db_record

    def update(self, idmapjnsd: int, map_jns_pendapatan: MapJnsPendapatan):
        db_record = self.get_by_id(idmapjnsd)
        if not db_record:
            return None

        for key, value in map_jns_pendapatan.__dict__.items():
            if key == "idmapjnsd":
                continue
            if value is not None:
                setattr(db_record, key, value)

        self.db.commit()
        self.db.refresh(db_record)
        return db_record

    def delete(self, idmapjnsd: int):
        db_record = self.get_by_id(idmapjnsd)
        if not db_record:
            return False
        self.db.delete(db_record)
        self.db.commit()
        return True
