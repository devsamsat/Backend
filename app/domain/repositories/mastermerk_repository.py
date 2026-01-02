from abc import ABC, abstractmethod
from typing import List, Optional

from app.domain.entities.mastermerk import MasterMerk


class MasterMerkRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[MasterMerk]:
        pass

    @abstractmethod
    def get_by_id(self, idmerk: int) -> Optional[MasterMerk]:
        pass

    @abstractmethod
    def create(self, master_merk: MasterMerk) -> MasterMerk:
        pass

    @abstractmethod
    def update(self, idmerk: int, master_merk: MasterMerk) -> Optional[MasterMerk]:
        pass

    @abstractmethod
    def delete(self, idmerk: int) -> bool:
        pass
