import json
from app.infrastructure.repositories.dynamic_record_repository import DynamicRecordRepository


class DynamicRecordUseCase:
    def __init__(self, repository: DynamicRecordRepository):
        self.repository = repository

    def get_all(self, table_name: str):
        return [self._serialize(record) for record in self.repository.get_all(table_name)]

    def get_by_record_id(self, table_name: str, record_id: str):
        record = self.repository.get_by_record_id(table_name, record_id)
        if not record:
            return None
        return self._serialize(record)

    def create(self, table_name: str, record_id: str, payload: dict):
        record = self.repository.create(table_name, record_id, payload)
        return self._serialize(record)

    def update(self, table_name: str, record_id: str, payload: dict):
        record = self.repository.get_by_record_id(table_name, record_id)
        if not record:
            return None
        record = self.repository.update(record, payload)
        return self._serialize(record)

    def delete(self, table_name: str, record_id: str):
        record = self.repository.get_by_record_id(table_name, record_id)
        if not record:
            return False
        return self.repository.delete(record)

    @staticmethod
    def _serialize(record):
        return {
            "id": record.id,
            "table_name": record.table_name,
            "record_id": record.record_id,
            "payload": json.loads(record.payload),
            "created_at": record.created_at,
            "updated_at": record.updated_at,
        }
