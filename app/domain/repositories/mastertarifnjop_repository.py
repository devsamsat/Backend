from abc import ABC, abstractmethod
from typing import List, Optional
from app.domain.entities.mastertarifnjop import MasterTarifNjop


class MasterTarifNjopRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[MasterTarifNjop]:
        pass

    @abstractmethod
    def get_by_id(self, idtarifnjop: int) -> Optional[MasterTarifNjop]:
        pass

    @abstractmethod
    def create(self, tarif: MasterTarifNjop) -> MasterTarifNjop:
        pass

    @abstractmethod
    def update(self, idtarifnjop: int, tarif: MasterTarifNjop) -> Optional[MasterTarifNjop]:
        pass

    @abstractmethod
    def delete(self, idtarifnjop: int) -> bool:
        pass
