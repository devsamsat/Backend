from abc import ABC, abstractmethod
from typing import List, Optional

from app.domain.entities.masterkecamatan import MasterKecamatan


class MasterKecamatanRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[MasterKecamatan]:
        pass

    @abstractmethod
    def get_by_id(self, idkecamatan: int) -> Optional[MasterKecamatan]:
        pass

    @abstractmethod
    def create(self, master_kecamatan: MasterKecamatan) -> MasterKecamatan:
        pass

    @abstractmethod
    def update(
        self,
        idkecamatan: int,
        master_kecamatan: MasterKecamatan,
    ) -> Optional[MasterKecamatan]:
        pass

    @abstractmethod
    def delete(self, idkecamatan: int) -> bool:
        pass
