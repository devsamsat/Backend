from abc import ABC, abstractmethod
from typing import List, Optional

from app.domain.entities.mapjnspendapatan import MapJnsPendapatan


class MapJnsPendapatanRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[MapJnsPendapatan]:
        pass

    @abstractmethod
    def get_by_id(self, idmapjnsd: int) -> Optional[MapJnsPendapatan]:
        pass

    @abstractmethod
    def create(self, map_jns_pendapatan: MapJnsPendapatan) -> MapJnsPendapatan:
        pass

    @abstractmethod
    def update(
        self,
        idmapjnsd: int,
        map_jns_pendapatan: MapJnsPendapatan,
    ) -> Optional[MapJnsPendapatan]:
        pass

    @abstractmethod
    def delete(self, idmapjnsd: int) -> bool:
        pass
