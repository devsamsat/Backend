from abc import ABC, abstractmethod
from typing import List, Optional
from app.domain.entities.dynamic_record import DynamicRecord


class DynamicRecordRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[DynamicRecord]:
        pass

    @abstractmethod
    def get_by_id(self, record_id: int) -> Optional[DynamicRecord]:
        pass

    @abstractmethod
    def create(self, record: DynamicRecord) -> DynamicRecord:
        pass

    @abstractmethod
    def update(self, record_id: int, record: DynamicRecord) -> Optional[DynamicRecord]:
        pass

    @abstractmethod
    def delete(self, record_id: int) -> bool:
        pass
