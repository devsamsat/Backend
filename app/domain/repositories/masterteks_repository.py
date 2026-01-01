from abc import ABC, abstractmethod
from typing import List, Optional
from app.domain.entities.masterteks import MasterTeks


class MasterTeksRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[MasterTeks]:
        pass

    @abstractmethod
    def get_by_id(self, idteks: int) -> Optional[MasterTeks]:
        pass

    @abstractmethod
    def create(self, teks: MasterTeks) -> MasterTeks:
        pass

    @abstractmethod
    def update(self, idteks: int, teks: MasterTeks) -> Optional[MasterTeks]:
        pass

    @abstractmethod
    def delete(self, idteks: int) -> bool:
        pass
