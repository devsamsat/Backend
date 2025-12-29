from __future__ import annotations

from typing import Any, Dict, Type

from app.core.table_constants import CUSTOM_TABLES
from app.domain.repositories.generated_table_repository import GeneratedTableRepository
from app.infrastructure.orm.table_registry import TABLE_NAMES


class BaseGeneratedTableUseCase:

    def __init__(self, repository: GeneratedTableRepository):
        self.repository = repository

    def get_all(self) -> list[Any]:
        return self.repository.get_all()

    def get_by_id(self, pk_values: dict[str, Any]) -> Any | None:
        return self.repository.get_by_id(pk_values)

    def create(self, entity: Any) -> Any:
        return self.repository.create(entity)

    def update(self, pk_values: dict[str, Any], entity: Any) -> Any | None:
        return self.repository.update(pk_values, entity)

    def delete(self, pk_values: dict[str, Any]) -> bool:
        return self.repository.delete(pk_values)


USECASE_REGISTRY: Dict[str, Type[BaseGeneratedTableUseCase]] = {}


def _to_camel(name: str) -> str:
    return "".join(part.capitalize() for part in name.split("_"))


for table_name in TABLE_NAMES:
    if table_name in CUSTOM_TABLES:
        continue
    class_name = f"{_to_camel(table_name)}UseCase"
    USECASE_REGISTRY[table_name] = type(
        class_name,
        (BaseGeneratedTableUseCase,),
        {},
    )


def get_usecase_class(table_name: str) -> Type[BaseGeneratedTableUseCase]:
    return USECASE_REGISTRY[table_name]
