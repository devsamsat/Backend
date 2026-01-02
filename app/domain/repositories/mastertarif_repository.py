from abc import ABC, abstractmethod
from typing import List, Optional

from app.domain.entities.mastertarif import MasterTarif


class MasterTarifRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[MasterTarif]:
        pass

    @abstractmethod
    def get_by_id(self, idtarif: int) -> Optional[MasterTarif]:
        pass

    @abstractmethod
    def create(self, master_tarif: MasterTarif) -> MasterTarif:
        pass

    @abstractmethod
    def update(self, idtarif: int, master_tarif: MasterTarif) -> Optional[MasterTarif]:
        pass

    @abstractmethod
    def delete(self, idtarif: int) -> bool:
        pass
