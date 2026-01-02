from abc import ABC, abstractmethod
from typing import List, Optional

from app.domain.entities.masterkbdet import MasterKbDet


class MasterKbDetRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[MasterKbDet]:
        pass

    @abstractmethod
    def get_by_id(self, idkbdet: int) -> Optional[MasterKbDet]:
        pass

    @abstractmethod
    def create(self, master_kbdet: MasterKbDet) -> MasterKbDet:
        pass

    @abstractmethod
    def update(self, idkbdet: int, master_kbdet: MasterKbDet) -> Optional[MasterKbDet]:
        pass

    @abstractmethod
    def delete(self, idkbdet: int) -> bool:
        pass
