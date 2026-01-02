from abc import ABC, abstractmethod
from typing import List, Optional

from app.domain.entities.transhistpenetapan import TransHistPenetapan


class TransHistPenetapanRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[TransHistPenetapan]:
        pass

    @abstractmethod
    def get_by_id(self, idhistpenetapan: int) -> Optional[TransHistPenetapan]:
        pass

    @abstractmethod
    def create(self, trans_hist_penetapan: TransHistPenetapan) -> TransHistPenetapan:
        pass

    @abstractmethod
    def update(
        self,
        idhistpenetapan: int,
        trans_hist_penetapan: TransHistPenetapan,
    ) -> Optional[TransHistPenetapan]:
        pass

    @abstractmethod
    def delete(self, idhistpenetapan: int) -> bool:
        pass
