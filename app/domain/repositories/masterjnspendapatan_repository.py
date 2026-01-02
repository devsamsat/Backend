from abc import ABC, abstractmethod
from typing import List, Optional

from app.domain.entities.masterjnspendapatan import MasterJnsPendapatan


class MasterJnsPendapatanRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[MasterJnsPendapatan]:
        pass

    @abstractmethod
    def get_by_id(self, idjnsd: int) -> Optional[MasterJnsPendapatan]:
        pass

    @abstractmethod
    def create(self, master_jns_pendapatan: MasterJnsPendapatan) -> MasterJnsPendapatan:
        pass

    @abstractmethod
    def update(
        self,
        idjnsd: int,
        master_jns_pendapatan: MasterJnsPendapatan,
    ) -> Optional[MasterJnsPendapatan]:
        pass

    @abstractmethod
    def delete(self, idjnsd: int) -> bool:
        pass
