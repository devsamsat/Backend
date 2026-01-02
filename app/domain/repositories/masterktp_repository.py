from abc import ABC, abstractmethod
from typing import List, Optional

from app.domain.entities.masterktp import MasterKtp


class MasterKtpRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[MasterKtp]:
        pass

    @abstractmethod
    def get_by_id(self, idktp: int) -> Optional[MasterKtp]:
        pass

    @abstractmethod
    def create(self, master_ktp: MasterKtp) -> MasterKtp:
        pass

    @abstractmethod
    def update(self, idktp: int, master_ktp: MasterKtp) -> Optional[MasterKtp]:
        pass

    @abstractmethod
    def delete(self, idktp: int) -> bool:
        pass
