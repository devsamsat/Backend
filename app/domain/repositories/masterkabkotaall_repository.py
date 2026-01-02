from abc import ABC, abstractmethod
from typing import List, Optional

from app.domain.entities.masterkabkotaall import MasterKabKotaAll


class MasterKabKotaAllRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[MasterKabKotaAll]:
        pass

    @abstractmethod
    def get_by_id(self, idkabkotaall: int) -> Optional[MasterKabKotaAll]:
        pass

    @abstractmethod
    def create(self, master_kabkotaall: MasterKabKotaAll) -> MasterKabKotaAll:
        pass

    @abstractmethod
    def update(
        self,
        idkabkotaall: int,
        master_kabkotaall: MasterKabKotaAll,
    ) -> Optional[MasterKabKotaAll]:
        pass

    @abstractmethod
    def delete(self, idkabkotaall: int) -> bool:
        pass
