from abc import ABC, abstractmethod
from typing import List, Optional

from app.domain.entities.masterbendahara import MasterBendahara


class MasterBendaharaRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[MasterBendahara]:
        pass

    @abstractmethod
    def get_by_id(self, idbend: int) -> Optional[MasterBendahara]:
        pass

    @abstractmethod
    def create(self, master_bendahara: MasterBendahara) -> MasterBendahara:
        pass

    @abstractmethod
    def update(self, idbend: int, master_bendahara: MasterBendahara) -> Optional[MasterBendahara]:
        pass

    @abstractmethod
    def delete(self, idbend: int) -> bool:
        pass
