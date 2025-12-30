from abc import ABC, abstractmethod
from typing import List, Optional

from app.domain.entities.masterhistory import MasterHistory


class MasterHistoryRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[MasterHistory]:
        pass

    @abstractmethod
    def get_by_id(self, idhistory: int) -> Optional[MasterHistory]:
        pass

    @abstractmethod
    def create(self, master_history: MasterHistory) -> MasterHistory:
        pass

    @abstractmethod
    def update(
        self,
        idhistory: int,
        master_history: MasterHistory,
    ) -> Optional[MasterHistory]:
        pass

    @abstractmethod
    def delete(self, idhistory: int) -> bool:
        pass
