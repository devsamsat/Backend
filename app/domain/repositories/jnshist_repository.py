from abc import ABC, abstractmethod
from typing import List, Optional
from app.domain.entities.jnshist import JnsHist


class JnsHistRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[JnsHist]:
        pass

    @abstractmethod
    def get_by_id(self, kdhist: str) -> Optional[JnsHist]:
        pass

    @abstractmethod
    def create(self, jnshist: JnsHist) -> JnsHist:
        pass

    @abstractmethod
    def update(self, kdhist: str, jnshist: JnsHist) -> Optional[JnsHist]:
        pass

    @abstractmethod
    def delete(self, kdhist: str) -> bool:
        pass
