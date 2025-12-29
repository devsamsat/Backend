from abc import ABC, abstractmethod
from typing import List, Optional
from app.domain.entities.jnsguna import JnsGuna


class JnsGunaRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[JnsGuna]:
        pass

    @abstractmethod
    def get_by_id(self, kdguna: str) -> Optional[JnsGuna]:
        pass

    @abstractmethod
    def create(self, jns_guna: JnsGuna) -> JnsGuna:
        pass

    @abstractmethod
    def update(self, kdguna: str, jns_guna: JnsGuna) -> Optional[JnsGuna]:
        pass

    @abstractmethod
    def delete(self, kdguna: str) -> bool:
        pass
