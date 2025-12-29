from abc import ABC, abstractmethod
from typing import Any, Optional


class GeneratedTableRepository(ABC):

    @abstractmethod
    def get_all(self) -> list[Any]:
        pass

    @abstractmethod
    def get_by_id(self, pk_values: dict[str, Any]) -> Optional[Any]:
        pass

    @abstractmethod
    def create(self, entity: Any) -> Any:
        pass

    @abstractmethod
    def update(self, pk_values: dict[str, Any], entity: Any) -> Optional[Any]:
        pass

    @abstractmethod
    def delete(self, pk_values: dict[str, Any]) -> bool:
        pass
