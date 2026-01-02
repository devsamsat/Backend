from abc import ABC, abstractmethod
from typing import List, Optional

from app.domain.entities.jnsstrurek import JnsStruRek


class JnsStruRekRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[JnsStruRek]:
        pass

    @abstractmethod
    def get_by_id(self, mtglevel: str) -> Optional[JnsStruRek]:
        pass

    @abstractmethod
    def create(self, jns_strurek: JnsStruRek) -> JnsStruRek:
        pass

    @abstractmethod
    def update(self, mtglevel: str, jns_strurek: JnsStruRek) -> Optional[JnsStruRek]:
        pass

    @abstractmethod
    def delete(self, mtglevel: str) -> bool:
        pass
