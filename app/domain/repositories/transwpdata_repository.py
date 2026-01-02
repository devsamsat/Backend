from abc import ABC, abstractmethod
from typing import List, Optional

from app.domain.entities.transwpdata import TransWpData


class TransWpDataRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[TransWpData]:
        pass

    @abstractmethod
    def get_by_id(self, idtwpdata: int) -> Optional[TransWpData]:
        pass

    @abstractmethod
    def create(self, trans_wpdata: TransWpData) -> TransWpData:
        pass

    @abstractmethod
    def update(
        self,
        idtwpdata: int,
        trans_wpdata: TransWpData,
    ) -> Optional[TransWpData]:
        pass

    @abstractmethod
    def delete(self, idtwpdata: int) -> bool:
        pass
