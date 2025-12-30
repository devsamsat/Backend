from typing import List
from app.domain.entities.appgroupuser import AppGroupUser
from app.domain.repositories.appgroupuser_repository import AppGroupUserRepository


class AppGroupUserUseCase:

    def __init__(self, repository: AppGroupUserRepository):
        self.repository = repository

    def get_all(self) -> List[AppGroupUser]:
        return self.repository.get_all()

    def get_by_id(self, kdgroup: str) -> AppGroupUser | None:
        return self.repository.get_by_id(kdgroup)

    def create(self, appgroupuser: AppGroupUser) -> AppGroupUser:
        return self.repository.create(appgroupuser)

    def update(self, kdgroup: str, appgroupuser: AppGroupUser) -> AppGroupUser | None:
        return self.repository.update(kdgroup, appgroupuser)

    def delete(self, kdgroup: str) -> bool:
        return self.repository.delete(kdgroup)
