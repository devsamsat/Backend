from abc import ABC, abstractmethod
from typing import List, Optional

from app.domain.entities.transpenetapan import TransPenetapan


class TransPenetapanRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[TransPenetapan]:
        pass

    @abstractmethod
    def get_by_id(self, idpenetapan: int) -> Optional[TransPenetapan]:
        pass

    @abstractmethod
    def create(self, trans_penetapan: TransPenetapan) -> TransPenetapan:
        pass

    @abstractmethod
    def update(
        self,
        idpenetapan: int,
        trans_penetapan: TransPenetapan,
    ) -> Optional[TransPenetapan]:
        pass

    @abstractmethod
    def delete(self, idpenetapan: int) -> bool:
        pass
