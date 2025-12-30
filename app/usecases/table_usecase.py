from typing import Any, Optional

from app.domain.entities.table_record import TableRecord
from app.domain.repositories.table_repository import TableRepository


class TableUseCase:
    def __init__(self, repository: TableRepository):
        self.repository = repository

    def get_all(self, table_name: str) -> list[TableRecord]:
        return self.repository.get_all(table_name)

    def get_by_id(self, table_name: str, pk_values: dict[str, Any]) -> Optional[TableRecord]:
        return self.repository.get_by_id(table_name, pk_values)

    def create(self, table_name: str, data: dict[str, Any]) -> TableRecord:
        return self.repository.create(table_name, data)

    def update(
        self,
        table_name: str,
        pk_values: dict[str, Any],
        data: dict[str, Any],
    ) -> Optional[TableRecord]:
        return self.repository.update(table_name, pk_values, data)

    def delete(self, table_name: str, pk_values: dict[str, Any]) -> bool:
        return self.repository.delete(table_name, pk_values)
