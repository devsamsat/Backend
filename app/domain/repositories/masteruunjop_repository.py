from abc import ABC, abstractmethod
from typing import List, Optional
from app.domain.entities.masteruunjop import MasterUuNjop


class MasterUuNjopRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[MasterUuNjop]:
        pass

    @abstractmethod
    def get_by_id(self, iduunjop: int) -> Optional[MasterUuNjop]:
        pass

    @abstractmethod
    def create(self, uu_njop: MasterUuNjop) -> MasterUuNjop:
        pass

    @abstractmethod
    def update(self, iduunjop: int, uu_njop: MasterUuNjop) -> Optional[MasterUuNjop]:
        pass

    @abstractmethod
    def delete(self, iduunjop: int) -> bool:
        pass
