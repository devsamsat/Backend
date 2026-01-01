from abc import ABC, abstractmethod
from typing import List, Optional
from app.domain.entities.masterwp import MasterWp


class MasterWpRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[MasterWp]:
        pass

    @abstractmethod
    def get_by_id(self, idwp: int) -> Optional[MasterWp]:
        pass

    @abstractmethod
    def create(self, wp: MasterWp) -> MasterWp:
        pass

    @abstractmethod
    def update(self, idwp: int, wp: MasterWp) -> Optional[MasterWp]:
        pass

    @abstractmethod
    def delete(self, idwp: int) -> bool:
        pass
