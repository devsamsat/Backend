from abc import ABC, abstractmethod
from typing import List, Optional

from app.domain.entities.jnsjr import JnsJr


class JnsJrRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[JnsJr]:
        pass

    @abstractmethod
    def get_by_id(self, jnsjrid: str) -> Optional[JnsJr]:
        pass

    @abstractmethod
    def create(self, jns_jr: JnsJr) -> JnsJr:
        pass

    @abstractmethod
    def update(self, jnsjrid: str, jns_jr: JnsJr) -> Optional[JnsJr]:
        pass

    @abstractmethod
    def delete(self, jnsjrid: str) -> bool:
        pass
