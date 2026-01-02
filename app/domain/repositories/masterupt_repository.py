from abc import ABC, abstractmethod
from typing import List, Optional

from app.domain.entities.masterupt import MasterUpt


class MasterUptRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[MasterUpt]:
        pass

    @abstractmethod
    def get_by_id(self, idupt: int) -> Optional[MasterUpt]:
        pass

    @abstractmethod
    def create(self, master_upt: MasterUpt) -> MasterUpt:
        pass

    @abstractmethod
    def update(self, idupt: int, master_upt: MasterUpt) -> Optional[MasterUpt]:
        pass

    @abstractmethod
    def delete(self, idupt: int) -> bool:
        pass
