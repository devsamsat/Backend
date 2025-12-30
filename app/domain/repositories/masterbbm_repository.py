from abc import ABC, abstractmethod
from typing import List, Optional

from app.domain.entities.masterbbm import MasterBbm


class MasterBbmRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[MasterBbm]:
        pass

    @abstractmethod
    def get_by_id(self, kodebbm: str) -> Optional[MasterBbm]:
        pass

    @abstractmethod
    def create(self, master_bbm: MasterBbm) -> MasterBbm:
        pass

    @abstractmethod
    def update(self, kodebbm: str, master_bbm: MasterBbm) -> Optional[MasterBbm]:
        pass

    @abstractmethod
    def delete(self, kodebbm: str) -> bool:
        pass
