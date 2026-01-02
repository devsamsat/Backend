from abc import ABC, abstractmethod
from typing import List, Optional

from app.domain.entities.jnsmilik import JnsMilik


class JnsMilikRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[JnsMilik]:
        pass

    @abstractmethod
    def get_by_id(self, kdmilik: str) -> Optional[JnsMilik]:
        pass

    @abstractmethod
    def create(self, jns_milik: JnsMilik) -> JnsMilik:
        pass

    @abstractmethod
    def update(self, kdmilik: str, jns_milik: JnsMilik) -> Optional[JnsMilik]:
        pass

    @abstractmethod
    def delete(self, kdmilik: str) -> bool:
        pass
