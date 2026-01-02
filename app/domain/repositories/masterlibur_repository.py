from abc import ABC, abstractmethod
from typing import List, Optional

from app.domain.entities.masterlibur import MasterLibur


class MasterLiburRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[MasterLibur]:
        pass

    @abstractmethod
    def get_by_id(self, idlibur: int) -> Optional[MasterLibur]:
        pass

    @abstractmethod
    def create(self, master_libur: MasterLibur) -> MasterLibur:
        pass

    @abstractmethod
    def update(self, idlibur: int, master_libur: MasterLibur) -> Optional[MasterLibur]:
        pass

    @abstractmethod
    def delete(self, idlibur: int) -> bool:
        pass
