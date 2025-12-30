from typing import List
from app.domain.entities.dynamic_record import DynamicRecord
from app.domain.repositories.dynamic_record_repository import DynamicRecordRepository


class DynamicRecordUseCase:
    def __init__(self, repository: DynamicRecordRepository):
        self.repository = repository

    def get_all(self) -> List[DynamicRecord]:
        return self.repository.get_all()

    def get_by_id(self, record_id: int) -> DynamicRecord | None:
        return self.repository.get_by_id(record_id)

    def create(self, table_name: str, record_id: str, payload: dict):
        record = DynamicRecord(
            id=None,
            table_name=table_name,
            record_id=record_id,
            payload=payload,
        )
        return self.repository.create(record)

    def update(
        self,
        record_id: int,
        table_name: str | None,
        new_record_id: str | None,
        payload: dict | None,
    ) -> DynamicRecord | None:
        record = DynamicRecord(
            id=record_id,
            table_name=table_name,
            record_id=new_record_id,
            payload=payload,
        )
        return self.repository.update(record_id, record)

    def delete(self, record_id: int) -> bool:
        return self.repository.delete(record_id)
