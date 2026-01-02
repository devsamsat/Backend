from abc import ABC, abstractmethod
from typing import List, Optional

from app.domain.entities.transsts import TransSts


class TransStsRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[TransSts]:
        pass

    @abstractmethod
    def get_by_id(self, idsts: int) -> Optional[TransSts]:
        pass

    @abstractmethod
    def create(self, trans_sts: TransSts) -> TransSts:
        pass

    @abstractmethod
    def update(self, idsts: int, trans_sts: TransSts) -> Optional[TransSts]:
        pass

    @abstractmethod
    def delete(self, idsts: int) -> bool:
        pass
