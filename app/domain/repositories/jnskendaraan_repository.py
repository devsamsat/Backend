from abc import ABC, abstractmethod
from typing import List, Optional

from app.domain.entities.jnskendaraan import JnsKendaraan


class JnsKendaraanRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[JnsKendaraan]:
        pass

    @abstractmethod
    def get_by_id(self, jnskendid: str) -> Optional[JnsKendaraan]:
        pass

    @abstractmethod
    def create(self, jns_kendaraan: JnsKendaraan) -> JnsKendaraan:
        pass

    @abstractmethod
    def update(
        self,
        jnskendid: str,
        jns_kendaraan: JnsKendaraan,
    ) -> Optional[JnsKendaraan]:
        pass

    @abstractmethod
    def delete(self, jnskendid: str) -> bool:
        pass
