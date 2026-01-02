from abc import ABC, abstractmethod
from typing import List, Optional

from app.domain.entities.masterwpdata import MasterWpData


class MasterWpDataRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[MasterWpData]:
        pass

    @abstractmethod
    def get_by_id(self, idwpdata: int) -> Optional[MasterWpData]:
        pass

    @abstractmethod
    def create(self, master_wpdata: MasterWpData) -> MasterWpData:
        pass

    @abstractmethod
    def update(self, idwpdata: int, master_wpdata: MasterWpData) -> Optional[MasterWpData]:
        pass

    @abstractmethod
    def delete(self, idwpdata: int) -> bool:
        pass
