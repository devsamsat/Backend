from abc import ABC, abstractmethod
from typing import List, Optional

from app.domain.entities.transwpdatafile import TransWpDataFile


class TransWpDataFileRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[TransWpDataFile]:
        pass

    @abstractmethod
    def get_by_id(self, idfile: int) -> Optional[TransWpDataFile]:
        pass

    @abstractmethod
    def create(self, trans_wpdatafile: TransWpDataFile) -> TransWpDataFile:
        pass

    @abstractmethod
    def update(
        self,
        idfile: int,
        trans_wpdatafile: TransWpDataFile,
    ) -> Optional[TransWpDataFile]:
        pass

    @abstractmethod
    def delete(self, idfile: int) -> bool:
        pass
