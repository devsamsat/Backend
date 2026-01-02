from abc import ABC, abstractmethod
from typing import List, Optional

from app.domain.entities.jnsprogresif import JnsProgresif


class JnsProgresifRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[JnsProgresif]:
        pass

    @abstractmethod
    def get_by_id(self, kdprogresif: int) -> Optional[JnsProgresif]:
        pass

    @abstractmethod
    def create(self, jns_progresif: JnsProgresif) -> JnsProgresif:
        pass

    @abstractmethod
    def update(
        self,
        kdprogresif: int,
        jns_progresif: JnsProgresif,
    ) -> Optional[JnsProgresif]:
        pass

    @abstractmethod
    def delete(self, kdprogresif: int) -> bool:
        pass
