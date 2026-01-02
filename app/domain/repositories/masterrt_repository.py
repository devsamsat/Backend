from abc import ABC, abstractmethod
from typing import List, Optional

from app.domain.entities.masterrt import MasterRt


class MasterRtRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[MasterRt]:
        pass

    @abstractmethod
    def get_by_id(self, idrt: int) -> Optional[MasterRt]:
        pass

    @abstractmethod
    def create(self, master_rt: MasterRt) -> MasterRt:
        pass

    @abstractmethod
    def update(self, idrt: int, master_rt: MasterRt) -> Optional[MasterRt]:
        pass

    @abstractmethod
    def delete(self, idrt: int) -> bool:
        pass
