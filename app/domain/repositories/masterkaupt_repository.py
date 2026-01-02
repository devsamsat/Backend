from abc import ABC, abstractmethod
from typing import List, Optional

from app.domain.entities.masterkaupt import MasterKaupt


class MasterKauptRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[MasterKaupt]:
        pass

    @abstractmethod
    def get_by_id(self, idkaupt: int) -> Optional[MasterKaupt]:
        pass

    @abstractmethod
    def create(self, master_kaupt: MasterKaupt) -> MasterKaupt:
        pass

    @abstractmethod
    def update(self, idkaupt: int, master_kaupt: MasterKaupt) -> Optional[MasterKaupt]:
        pass

    @abstractmethod
    def delete(self, idkaupt: int) -> bool:
        pass
