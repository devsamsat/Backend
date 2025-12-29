from abc import ABC, abstractmethod
from typing import Any, Optional

from app.domain.entities.table_record import TableRecord


class TableRepository(ABC):

    @abstractmethod
    def get_all(self, table_name: str) -> list[TableRecord]:
        pass

    @abstractmethod
    def get_by_id(self, table_name: str, pk_values: dict[str, Any]) -> Optional[TableRecord]:
        pass

    @abstractmethod
    def create(self, table_name: str, data: dict[str, Any]) -> TableRecord:
        pass

    @abstractmethod
    def update(
        self,
        table_name: str,
        pk_values: dict[str, Any],
        data: dict[str, Any],
    ) -> Optional[TableRecord]:
        pass

    @abstractmethod
    def delete(self, table_name: str, pk_values: dict[str, Any]) -> bool:
        pass
