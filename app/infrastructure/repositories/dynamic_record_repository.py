import json
from sqlalchemy.orm import Session
from app.infrastructure.orm.models import DynamicRecord


class DynamicRecordRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self, table_name: str):
        return (
            self.db.query(DynamicRecord)
            .filter(DynamicRecord.table_name == table_name)
            .order_by(DynamicRecord.id.asc())
            .all()
        )

    def get_by_record_id(self, table_name: str, record_id: str):
        return (
            self.db.query(DynamicRecord)
            .filter(
                DynamicRecord.table_name == table_name,
                DynamicRecord.record_id == record_id,
            )
            .first()
        )

    def create(self, table_name: str, record_id: str, payload: dict):
        record = DynamicRecord(
            table_name=table_name,
            record_id=record_id,
            payload=json.dumps(payload),
        )
        self.db.add(record)
        self.db.commit()
        self.db.refresh(record)
        return record

    def update(self, record: DynamicRecord, payload: dict):
        record.payload = json.dumps(payload)
        self.db.commit()
        self.db.refresh(record)
        return record

    def delete(self, record: DynamicRecord):
        self.db.delete(record)
        self.db.commit()
        return True
