from abc import ABC, abstractmethod
from typing import List, Optional

from app.domain.entities.masteruunjop import MasterUunJop


class MasterUunJopRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[MasterUunJop]:
        pass

    @abstractmethod
    def get_by_id(self, iduunjop: int) -> Optional[MasterUunJop]:
        pass

    @abstractmethod
    def create(self, master_uun_jop: MasterUunJop) -> MasterUunJop:
        pass

    @abstractmethod
    def update(
        self,
        iduunjop: int,
        master_uun_jop: MasterUunJop,
    ) -> Optional[MasterUunJop]:
        pass

    @abstractmethod
    def delete(self, iduunjop: int) -> bool:
        pass
