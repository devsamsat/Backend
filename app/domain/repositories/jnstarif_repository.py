from abc import ABC, abstractmethod
from typing import List, Optional

from app.domain.entities.jnstarif import JnsTarif


class JnsTarifRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[JnsTarif]:
        pass

    @abstractmethod
    def get_by_id(self, kdjnstarif: str) -> Optional[JnsTarif]:
        pass

    @abstractmethod
    def create(self, jns_tarif: JnsTarif) -> JnsTarif:
        pass

    @abstractmethod
    def update(self, kdjnstarif: str, jns_tarif: JnsTarif) -> Optional[JnsTarif]:
        pass

    @abstractmethod
    def delete(self, kdjnstarif: str) -> bool:
        pass
