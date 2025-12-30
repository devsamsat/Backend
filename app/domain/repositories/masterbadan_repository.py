from abc import ABC, abstractmethod
from typing import List, Optional

from app.domain.entities.masterbadan import MasterBadan


class MasterBadanRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[MasterBadan]:
        pass

    @abstractmethod
    def get_by_id(self, idbadan: int) -> Optional[MasterBadan]:
        pass

    @abstractmethod
    def create(self, master_badan: MasterBadan) -> MasterBadan:
        pass

    @abstractmethod
    def update(self, idbadan: int, master_badan: MasterBadan) -> Optional[MasterBadan]:
        pass

    @abstractmethod
    def delete(self, idbadan: int) -> bool:
        pass
