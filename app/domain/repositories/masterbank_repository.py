from abc import ABC, abstractmethod
from typing import List, Optional

from app.domain.entities.masterbank import MasterBank


class MasterBankRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[MasterBank]:
        pass

    @abstractmethod
    def get_by_id(self, idbank: int) -> Optional[MasterBank]:
        pass

    @abstractmethod
    def create(self, master_bank: MasterBank) -> MasterBank:
        pass

    @abstractmethod
    def update(self, idbank: int, master_bank: MasterBank) -> Optional[MasterBank]:
        pass

    @abstractmethod
    def delete(self, idbank: int) -> bool:
        pass
