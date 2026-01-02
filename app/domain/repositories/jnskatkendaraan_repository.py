from abc import ABC, abstractmethod
from typing import List, Optional

from app.domain.entities.jnskatkendaraan import JnsKatKendaraan


class JnsKatKendaraanRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[JnsKatKendaraan]:
        pass

    @abstractmethod
    def get_by_id(self, katid: str) -> Optional[JnsKatKendaraan]:
        pass

    @abstractmethod
    def create(self, jns_katkendaraan: JnsKatKendaraan) -> JnsKatKendaraan:
        pass

    @abstractmethod
    def update(
        self,
        katid: str,
        jns_katkendaraan: JnsKatKendaraan,
    ) -> Optional[JnsKatKendaraan]:
        pass

    @abstractmethod
    def delete(self, katid: str) -> bool:
        pass
