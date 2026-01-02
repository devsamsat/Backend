from abc import ABC, abstractmethod
from typing import List, Optional

from app.domain.entities.masterrw import MasterRw


class MasterRwRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[MasterRw]:
        pass

    @abstractmethod
    def get_by_id(self, idrw: int) -> Optional[MasterRw]:
        pass

    @abstractmethod
    def create(self, master_rw: MasterRw) -> MasterRw:
        pass

    @abstractmethod
    def update(self, idrw: int, master_rw: MasterRw) -> Optional[MasterRw]:
        pass

    @abstractmethod
    def delete(self, idrw: int) -> bool:
        pass
