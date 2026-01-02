from abc import ABC, abstractmethod
from typing import List, Optional

from app.domain.entities.masterkabkota import MasterKabKota


class MasterKabKotaRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[MasterKabKota]:
        pass

    @abstractmethod
    def get_by_id(self, idkabkota: int) -> Optional[MasterKabKota]:
        pass

    @abstractmethod
    def create(self, master_kabkota: MasterKabKota) -> MasterKabKota:
        pass

    @abstractmethod
    def update(
        self,
        idkabkota: int,
        master_kabkota: MasterKabKota,
    ) -> Optional[MasterKabKota]:
        pass

    @abstractmethod
    def delete(self, idkabkota: int) -> bool:
        pass
