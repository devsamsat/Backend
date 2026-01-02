from abc import ABC, abstractmethod
from typing import List, Optional

from app.domain.entities.masterrekd import MasterRekd


class MasterRekdRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[MasterRekd]:
        pass

    @abstractmethod
    def get_by_id(self, idrekd: int) -> Optional[MasterRekd]:
        pass

    @abstractmethod
    def create(self, master_rekd: MasterRekd) -> MasterRekd:
        pass

    @abstractmethod
    def update(self, idrekd: int, master_rekd: MasterRekd) -> Optional[MasterRekd]:
        pass

    @abstractmethod
    def delete(self, idrekd: int) -> bool:
        pass
