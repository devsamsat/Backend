from typing import List
from app.domain.entities.appuser import AppUser
from app.domain.repositories.appuser_repository import AppUserRepository


class AppUserUseCase:

    def __init__(self, repository: AppUserRepository):
        self.repository = repository

    def get_all(self) -> List[AppUser]:
        return self.repository.get_all()

    def get_by_id(self, userid: str) -> AppUser | None:
        return self.repository.get_by_id(userid)

    def create(self, appuser: AppUser) -> AppUser:
        return self.repository.create(appuser)

    def update(self, userid: str, appuser: AppUser) -> AppUser | None:
        return self.repository.update(userid, appuser)

    def delete(self, userid: str) -> bool:
        return self.repository.delete(userid)
