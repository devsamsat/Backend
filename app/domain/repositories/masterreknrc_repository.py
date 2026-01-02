from abc import ABC, abstractmethod
from typing import List, Optional

from app.domain.entities.masterreknrc import MasterRekNrc


class MasterRekNrcRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[MasterRekNrc]:
        pass

    @abstractmethod
    def get_by_id(self, idreknrc: int) -> Optional[MasterRekNrc]:
        pass

    @abstractmethod
    def create(self, master_reknrc: MasterRekNrc) -> MasterRekNrc:
        pass

    @abstractmethod
    def update(
        self,
        idreknrc: int,
        master_reknrc: MasterRekNrc,
    ) -> Optional[MasterRekNrc]:
        pass

    @abstractmethod
    def delete(self, idreknrc: int) -> bool:
        pass
