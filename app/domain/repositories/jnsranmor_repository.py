from abc import ABC, abstractmethod
from typing import List, Optional

from app.domain.entities.jnsranmor import JnsRanmor


class JnsRanmorRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[JnsRanmor]:
        pass

    @abstractmethod
    def get_by_id(self, kdranmor: str) -> Optional[JnsRanmor]:
        pass

    @abstractmethod
    def create(self, jns_ranmor: JnsRanmor) -> JnsRanmor:
        pass

    @abstractmethod
    def update(self, kdranmor: str, jns_ranmor: JnsRanmor) -> Optional[JnsRanmor]:
        pass

    @abstractmethod
    def delete(self, kdranmor: str) -> bool:
        pass
