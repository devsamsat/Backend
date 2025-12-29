from abc import ABC, abstractmethod
from typing import List, Optional
from app.domain.entities.approle import AppRole


class AppRoleRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[AppRole]:
        pass

    @abstractmethod
    def get_by_id(self, roleid: str) -> Optional[AppRole]:
        pass

    @abstractmethod
    def create(self, app_role: AppRole) -> AppRole:
        pass

    @abstractmethod
    def update(self, roleid: str, app_role: AppRole) -> Optional[AppRole]:
        pass

    @abstractmethod
    def delete(self, roleid: str) -> bool:
        pass
