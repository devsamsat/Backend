from abc import ABC, abstractmethod
from typing import List, Optional

from app.domain.entities.masterkiosk import MasterKiosk


class MasterKioskRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[MasterKiosk]:
        pass

    @abstractmethod
    def get_by_id(self, idkios: int) -> Optional[MasterKiosk]:
        pass

    @abstractmethod
    def create(self, master_kiosk: MasterKiosk) -> MasterKiosk:
        pass

    @abstractmethod
    def update(self, idkios: int, master_kiosk: MasterKiosk) -> Optional[MasterKiosk]:
        pass

    @abstractmethod
    def delete(self, idkios: int) -> bool:
        pass
