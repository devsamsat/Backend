from abc import ABC, abstractmethod
from typing import List, Optional

from app.domain.entities.jnsplat import JnsPlat


class JnsPlatRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[JnsPlat]:
        pass

    @abstractmethod
    def get_by_id(self, kdplat: str) -> Optional[JnsPlat]:
        pass

    @abstractmethod
    def create(self, jns_plat: JnsPlat) -> JnsPlat:
        pass

    @abstractmethod
    def update(self, kdplat: str, jns_plat: JnsPlat) -> Optional[JnsPlat]:
        pass

    @abstractmethod
    def delete(self, kdplat: str) -> bool:
        pass
