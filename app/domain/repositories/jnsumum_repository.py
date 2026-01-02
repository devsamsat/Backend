from abc import ABC, abstractmethod
from typing import List, Optional

from app.domain.entities.jnsumum import JnsUmum


class JnsUmumRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[JnsUmum]:
        pass

    @abstractmethod
    def get_by_id(self, kdumum: str) -> Optional[JnsUmum]:
        pass

    @abstractmethod
    def create(self, jns_umum: JnsUmum) -> JnsUmum:
        pass

    @abstractmethod
    def update(self, kdumum: str, jns_umum: JnsUmum) -> Optional[JnsUmum]:
        pass

    @abstractmethod
    def delete(self, kdumum: str) -> bool:
        pass
