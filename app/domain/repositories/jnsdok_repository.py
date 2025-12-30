from abc import ABC, abstractmethod
from typing import List, Optional
from app.domain.entities.jnsdok import JnsDok


class JnsDokRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[JnsDok]:
        pass

    @abstractmethod
    def get_by_id(self, kddok: str) -> Optional[JnsDok]:
        pass

    @abstractmethod
    def create(self, jnsdok: JnsDok) -> JnsDok:
        pass

    @abstractmethod
    def update(self, kddok: str, jnsdok: JnsDok) -> Optional[JnsDok]:
        pass

    @abstractmethod
    def delete(self, kddok: str) -> bool:
        pass
