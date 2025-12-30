from typing import List
from app.domain.entities.approle import AppRole
from app.domain.repositories.approle_repository import AppRoleRepository


class AppRoleUseCase:

    def __init__(self, repository: AppRoleRepository):
        self.repository = repository

    def get_all(self) -> List[AppRole]:
        return self.repository.get_all()

    def get_by_id(self, roleid: str) -> AppRole | None:
        return self.repository.get_by_id(roleid)

    def create(self, approle: AppRole) -> AppRole:
        return self.repository.create(approle)

    def update(self, roleid: str, approle: AppRole) -> AppRole | None:
        return self.repository.update(roleid, approle)

    def delete(self, roleid: str) -> bool:
        return self.repository.delete(roleid)
