from abc import ABC, abstractmethod
from typing import List, Optional

from app.domain.entities.masterprovinsi import MasterProvinsi


class MasterProvinsiRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[MasterProvinsi]:
        pass

    @abstractmethod
    def get_by_id(self, idprovinsi: int) -> Optional[MasterProvinsi]:
        pass

    @abstractmethod
    def create(self, master_provinsi: MasterProvinsi) -> MasterProvinsi:
        pass

    @abstractmethod
    def update(
        self,
        idprovinsi: int,
        master_provinsi: MasterProvinsi,
    ) -> Optional[MasterProvinsi]:
        pass

    @abstractmethod
    def delete(self, idprovinsi: int) -> bool:
        pass
