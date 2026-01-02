from abc import ABC, abstractmethod
from typing import List, Optional

from app.domain.entities.transwpdataantri import TransWpDataAntri


class TransWpDataAntriRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[TransWpDataAntri]:
        pass

    @abstractmethod
    def get_by_id(self, idantri: int) -> Optional[TransWpDataAntri]:
        pass

    @abstractmethod
    def create(self, trans_wpdataantri: TransWpDataAntri) -> TransWpDataAntri:
        pass

    @abstractmethod
    def update(
        self,
        idantri: int,
        trans_wpdataantri: TransWpDataAntri,
    ) -> Optional[TransWpDataAntri]:
        pass

    @abstractmethod
    def delete(self, idantri: int) -> bool:
        pass
