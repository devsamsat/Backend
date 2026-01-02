from abc import ABC, abstractmethod
from typing import List, Optional

from app.domain.entities.transstsdet import TransStsDet


class TransStsDetRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[TransStsDet]:
        pass

    @abstractmethod
    def get_by_id(self, idstsdet: int) -> Optional[TransStsDet]:
        pass

    @abstractmethod
    def create(self, trans_sts_det: TransStsDet) -> TransStsDet:
        pass

    @abstractmethod
    def update(
        self,
        idstsdet: int,
        trans_sts_det: TransStsDet,
    ) -> Optional[TransStsDet]:
        pass

    @abstractmethod
    def delete(self, idstsdet: int) -> bool:
        pass
