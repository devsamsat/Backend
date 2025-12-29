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

    def create(
        self,
        kdgroup: str,
        nmgroup: str,
        ket: str | None,
        created_by: str | None,
        updated_by: str | None,
    ) -> AppGroupUser:
        group_user = AppGroupUser(
            kdgroup=kdgroup,
            nmgroup=nmgroup,
            ket=ket,
            created_by=created_by,
            updated_by=updated_by,
        )
        return self.repository.create(group_user)

    def update(
        self,
        kdgroup: str,
        nmgroup: str | None,
        ket: str | None,
        updated_by: str | None,
    ) -> AppGroupUser | None:
        group_user = AppGroupUser(
            kdgroup=kdgroup,
            nmgroup=nmgroup,
            ket=ket,
            updated_by=updated_by,
        )
        return self.repository.update(kdgroup, group_user)

    def delete(self, kdgroup: str) -> bool:
        return self.repository.delete(kdgroup)
