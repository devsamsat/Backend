from abc import ABC, abstractmethod
from typing import List, Optional
from app.domain.entities.appotor import AppOtor


class AppOtorRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[AppOtor]:
        pass

    @abstractmethod
    def get_by_id(self, kdgroup: str, roleid: str) -> Optional[AppOtor]:
        pass

    @abstractmethod
    def create(self, appotor: AppOtor) -> AppOtor:
        pass

    @abstractmethod
    def update(
        self,
        kdgroup: str,
        roleid: str,
        appotor: AppOtor,
    ) -> Optional[AppOtor]:
        pass

    @abstractmethod
    def delete(self, kdgroup: str, roleid: str) -> bool:
        pass
