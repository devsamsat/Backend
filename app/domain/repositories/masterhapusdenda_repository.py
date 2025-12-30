from abc import ABC, abstractmethod
from typing import List, Optional

from app.domain.entities.masterhapusdenda import MasterHapusDenda


class MasterHapusDendaRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[MasterHapusDenda]:
        pass

    @abstractmethod
    def get_by_id(self, idhapusdenda: int) -> Optional[MasterHapusDenda]:
        pass

    @abstractmethod
    def create(self, master_hapus_denda: MasterHapusDenda) -> MasterHapusDenda:
        pass

    @abstractmethod
    def update(
        self,
        idhapusdenda: int,
        master_hapus_denda: MasterHapusDenda,
    ) -> Optional[MasterHapusDenda]:
        pass

    @abstractmethod
    def delete(self, idhapusdenda: int) -> bool:
        pass
