from abc import ABC, abstractmethod
from typing import List, Optional

from app.domain.entities.transhistpendataandet import TransHistPendataanDet


class TransHistPendataanDetRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[TransHistPendataanDet]:
        pass

    @abstractmethod
    def get_by_id(self, idhistpendataandet: int) -> Optional[TransHistPendataanDet]:
        pass

    @abstractmethod
    def create(
        self,
        trans_hist_pendataan_det: TransHistPendataanDet,
    ) -> TransHistPendataanDet:
        pass

    @abstractmethod
    def update(
        self,
        idhistpendataandet: int,
        trans_hist_pendataan_det: TransHistPendataanDet,
    ) -> Optional[TransHistPendataanDet]:
        pass

    @abstractmethod
    def delete(self, idhistpendataandet: int) -> bool:
        pass
