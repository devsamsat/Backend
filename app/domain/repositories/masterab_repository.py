from abc import ABC, abstractmethod
from typing import List, Optional

from app.domain.entities.masterab import MasterAb


class MasterAbRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[MasterAb]:
        pass

    @abstractmethod
    def get_by_id(self, idab: int) -> Optional[MasterAb]:
        pass

    @abstractmethod
    def create(self, master_ab: MasterAb) -> MasterAb:
        pass

    @abstractmethod
    def update(self, idab: int, master_ab: MasterAb) -> Optional[MasterAb]:
        pass

    @abstractmethod
    def delete(self, idab: int) -> bool:
        pass
