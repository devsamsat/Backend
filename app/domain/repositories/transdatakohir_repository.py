from abc import ABC, abstractmethod
from typing import List, Optional
from app.domain.entities.transdatakohir import TransDataKohir


class TransDataKohirRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[TransDataKohir]:
        pass

    @abstractmethod
    def get_by_id(self, idkohir: int) -> Optional[TransDataKohir]:
        pass

    @abstractmethod
    def create(self, kohir: TransDataKohir) -> TransDataKohir:
        pass

    @abstractmethod
    def update(self, idkohir: int, kohir: TransDataKohir) -> Optional[TransDataKohir]:
        pass

    @abstractmethod
    def delete(self, idkohir: int) -> bool:
        pass
