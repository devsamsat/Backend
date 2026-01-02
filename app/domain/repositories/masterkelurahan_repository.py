from abc import ABC, abstractmethod
from typing import List, Optional

from app.domain.entities.masterkelurahan import MasterKelurahan


class MasterKelurahanRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[MasterKelurahan]:
        pass

    @abstractmethod
    def get_by_id(self, idkelurahan: int) -> Optional[MasterKelurahan]:
        pass

    @abstractmethod
    def create(self, master_kelurahan: MasterKelurahan) -> MasterKelurahan:
        pass

    @abstractmethod
    def update(
        self,
        idkelurahan: int,
        master_kelurahan: MasterKelurahan,
    ) -> Optional[MasterKelurahan]:
        pass

    @abstractmethod
    def delete(self, idkelurahan: int) -> bool:
        pass
