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

    def create(
        self,
        roleid: str,
        idapp: int | None,
        role: str | None,
        role_type: str | None,
        menuid: str | None,
        parentid: str | None,
        bantuan: str | None,
        link: str | None,
        icon: str | None,
        kdlevel: int | None,
        is_show: int | None,
        created_by: str | None,
        updated_by: str | None,
    ) -> AppRole:
        app_role = AppRole(
            roleid=roleid,
            idapp=idapp,
            role=role,
            role_type=role_type,
            menuid=menuid,
            parentid=parentid,
            bantuan=bantuan,
            link=link,
            icon=icon,
            kdlevel=kdlevel,
            is_show=is_show,
            created_by=created_by,
            updated_by=updated_by,
        )
        return self.repository.create(app_role)

    def update(
        self,
        roleid: str,
        idapp: int | None,
        role: str | None,
        role_type: str | None,
        menuid: str | None,
        parentid: str | None,
        bantuan: str | None,
        link: str | None,
        icon: str | None,
        kdlevel: int | None,
        is_show: int | None,
        updated_by: str | None,
    ) -> AppRole | None:
        app_role = AppRole(
            roleid=roleid,
            idapp=idapp,
            role=role,
            role_type=role_type,
            menuid=menuid,
            parentid=parentid,
            bantuan=bantuan,
            link=link,
            icon=icon,
            kdlevel=kdlevel,
            is_show=is_show,
            updated_by=updated_by,
        )
        return self.repository.update(roleid, app_role)

    def delete(self, roleid: str) -> bool:
        return self.repository.delete(roleid)
