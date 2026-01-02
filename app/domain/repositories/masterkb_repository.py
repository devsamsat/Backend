from abc import ABC, abstractmethod
from typing import List, Optional

from app.domain.entities.masterkb import MasterKb


class MasterKbRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[MasterKb]:
        pass

    @abstractmethod
    def get_by_id(self, idkb: int) -> Optional[MasterKb]:
        pass

    @abstractmethod
    def create(self, master_kb: MasterKb) -> MasterKb:
        pass

    @abstractmethod
    def update(self, idkb: int, master_kb: MasterKb) -> Optional[MasterKb]:
        pass

    @abstractmethod
    def delete(self, idkb: int) -> bool:
        pass
