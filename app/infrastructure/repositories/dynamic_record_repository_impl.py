import json
from sqlalchemy.orm import Session
from app.domain.entities.dynamic_record import DynamicRecord
from app.domain.repositories.dynamic_record_repository import DynamicRecordRepository
from app.infrastructure.orm.models import DynamicRecord as DynamicRecordModel


class DynamicRecordRepositoryImpl(DynamicRecordRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(DynamicRecordModel).order_by(DynamicRecordModel.id.asc()).all()

    def get_by_id(self, record_id: int):
        return (
            self.db.query(DynamicRecordModel)
            .filter(DynamicRecordModel.id == record_id)
            .first()
        )

    def create(self, record: DynamicRecord):
        db_record = DynamicRecordModel(
            table_name=record.table_name,
            record_id=record.record_id,
            payload=json.dumps(record.payload),
        )
        self.db.add(db_record)
        self.db.commit()
        self.db.refresh(db_record)
        return db_record

    def update(self, record_id: int, record: DynamicRecord):
        db_record = self.get_by_id(record_id)
        if not db_record:
            return None

        if record.table_name is not None:
            db_record.table_name = record.table_name
        if record.record_id is not None:
            db_record.record_id = record.record_id
        if record.payload is not None:
            db_record.payload = json.dumps(record.payload)

        self.db.commit()
        self.db.refresh(db_record)
        return db_record

    def delete(self, record_id: int):
        db_record = self.get_by_id(record_id)
        if not db_record:
            return False
        self.db.delete(db_record)
        self.db.commit()
        return True
