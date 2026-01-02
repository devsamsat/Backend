from abc import ABC, abstractmethod
from typing import List, Optional

from app.domain.entities.jnspajak import JnsPajak


class JnsPajakRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[JnsPajak]:
        pass

    @abstractmethod
    def get_by_id(self, kdjnspjk: str) -> Optional[JnsPajak]:
        pass

    @abstractmethod
    def create(self, jns_pajak: JnsPajak) -> JnsPajak:
        pass

    @abstractmethod
    def update(self, kdjnspjk: str, jns_pajak: JnsPajak) -> Optional[JnsPajak]:
        pass

    @abstractmethod
    def delete(self, kdjnspjk: str) -> bool:
        pass
