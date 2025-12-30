from abc import ABC, abstractmethod
from typing import List, Optional

from app.domain.entities.masterflow import MasterFlow


class MasterFlowRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[MasterFlow]:
        pass

    @abstractmethod
    def get_by_id(self, kdflow: str) -> Optional[MasterFlow]:
        pass

    @abstractmethod
    def create(self, master_flow: MasterFlow) -> MasterFlow:
        pass

    @abstractmethod
    def update(self, kdflow: str, master_flow: MasterFlow) -> Optional[MasterFlow]:
        pass

    @abstractmethod
    def delete(self, kdflow: str) -> bool:
        pass
