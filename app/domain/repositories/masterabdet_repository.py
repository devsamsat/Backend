from abc import ABC, abstractmethod
from typing import List, Optional

from app.domain.entities.masterabdet import MasterAbDet


class MasterAbDetRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[MasterAbDet]:
        pass

    @abstractmethod
    def get_by_id(self, idabdet: int) -> Optional[MasterAbDet]:
        pass

    @abstractmethod
    def create(self, master_ab_det: MasterAbDet) -> MasterAbDet:
        pass

    @abstractmethod
    def update(self, idabdet: int, master_ab_det: MasterAbDet) -> Optional[MasterAbDet]:
        pass

    @abstractmethod
    def delete(self, idabdet: int) -> bool:
        pass
