from abc import ABC, abstractmethod
from typing import List, Optional

from app.domain.entities.masterjabttd import MasterJabTtd


class MasterJabTtdRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[MasterJabTtd]:
        pass

    @abstractmethod
    def get_by_id(self, idjabttd: int) -> Optional[MasterJabTtd]:
        pass

    @abstractmethod
    def create(self, master_jab_ttd: MasterJabTtd) -> MasterJabTtd:
        pass

    @abstractmethod
    def update(
        self,
        idjabttd: int,
        master_jab_ttd: MasterJabTtd,
    ) -> Optional[MasterJabTtd]:
        pass

    @abstractmethod
    def delete(self, idjabttd: int) -> bool:
        pass
