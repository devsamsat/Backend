from abc import ABC, abstractmethod
from typing import List, Optional
from app.domain.entities.appgroupuser import AppGroupUser


class AppGroupUserRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[AppGroupUser]:
        pass

    @abstractmethod
    def get_by_id(self, kdgroup: str) -> Optional[AppGroupUser]:
        pass

    @abstractmethod
    def create(self, group_user: AppGroupUser) -> AppGroupUser:
        pass

    @abstractmethod
    def update(self, kdgroup: str, group_user: AppGroupUser) -> Optional[AppGroupUser]:
        pass

    @abstractmethod
    def delete(self, kdgroup: str) -> bool:
        pass
