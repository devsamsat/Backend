from abc import ABC, abstractmethod
from typing import List, Optional

from app.domain.entities.masternpwpd import MasterNpwpd


class MasterNpwpdRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[MasterNpwpd]:
        pass

    @abstractmethod
    def get_by_id(self, idnpwpd: int) -> Optional[MasterNpwpd]:
        pass

    @abstractmethod
    def create(self, master_npwpd: MasterNpwpd) -> MasterNpwpd:
        pass

    @abstractmethod
    def update(self, idnpwpd: int, master_npwpd: MasterNpwpd) -> Optional[MasterNpwpd]:
        pass

    @abstractmethod
    def delete(self, idnpwpd: int) -> bool:
        pass
