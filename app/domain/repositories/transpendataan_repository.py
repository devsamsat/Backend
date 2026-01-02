from abc import ABC, abstractmethod
from typing import List, Optional

from app.domain.entities.transpendataan import TransPendataan


class TransPendataanRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[TransPendataan]:
        pass

    @abstractmethod
    def get_by_id(self, idpendataan: int) -> Optional[TransPendataan]:
        pass

    @abstractmethod
    def create(self, trans_pendataan: TransPendataan) -> TransPendataan:
        pass

    @abstractmethod
    def update(
        self,
        idpendataan: int,
        trans_pendataan: TransPendataan,
    ) -> Optional[TransPendataan]:
        pass

    @abstractmethod
    def delete(self, idpendataan: int) -> bool:
        pass
