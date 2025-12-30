from abc import ABC, abstractmethod
from typing import List, Optional
from app.domain.entities.appuser import AppUser


class AppUserRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[AppUser]:
        pass

    @abstractmethod
    def get_by_id(self, userid: str) -> Optional[AppUser]:
        pass

    @abstractmethod
    def create(self, appuser: AppUser) -> AppUser:
        pass

    @abstractmethod
    def update(self, userid: str, appuser: AppUser) -> Optional[AppUser]:
        pass

    @abstractmethod
    def delete(self, userid: str) -> bool:
        pass
