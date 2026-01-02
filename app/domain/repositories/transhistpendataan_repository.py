from abc import ABC, abstractmethod
from typing import List, Optional

from app.domain.entities.transhistpendataan import TransHistPendataan


class TransHistPendataanRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[TransHistPendataan]:
        pass

    @abstractmethod
    def get_by_id(self, idhistpendataan: int) -> Optional[TransHistPendataan]:
        pass

    @abstractmethod
    def create(self, trans_hist_pendataan: TransHistPendataan) -> TransHistPendataan:
        pass

    @abstractmethod
    def update(
        self,
        idhistpendataan: int,
        trans_hist_pendataan: TransHistPendataan,
    ) -> Optional[TransHistPendataan]:
        pass

    @abstractmethod
    def delete(self, idhistpendataan: int) -> bool:
        pass
