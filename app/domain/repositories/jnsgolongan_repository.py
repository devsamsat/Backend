from abc import ABC, abstractmethod
from typing import List, Optional
from app.domain.entities.jnsgolongan import JnsGolongan


class JnsGolonganRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[JnsGolongan]:
        pass

    @abstractmethod
    def get_by_id(self, jnsgolid: str) -> Optional[JnsGolongan]:
        pass

    @abstractmethod
    def create(self, jns_golongan: JnsGolongan) -> JnsGolongan:
        pass

    @abstractmethod
    def update(self, jnsgolid: str, jns_golongan: JnsGolongan) -> Optional[JnsGolongan]:
        pass

    @abstractmethod
    def delete(self, jnsgolid: str) -> bool:
        pass
