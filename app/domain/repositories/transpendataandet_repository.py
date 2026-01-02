from abc import ABC, abstractmethod
from typing import List, Optional

from app.domain.entities.transpendataandet import TransPendataanDet


class TransPendataanDetRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[TransPendataanDet]:
        pass

    @abstractmethod
    def get_by_id(self, idpendataandet: int) -> Optional[TransPendataanDet]:
        pass

    @abstractmethod
    def create(self, trans_pendataan_det: TransPendataanDet) -> TransPendataanDet:
        pass

    @abstractmethod
    def update(
        self,
        idpendataandet: int,
        trans_pendataan_det: TransPendataanDet,
    ) -> Optional[TransPendataanDet]:
        pass

    @abstractmethod
    def delete(self, idpendataandet: int) -> bool:
        pass
