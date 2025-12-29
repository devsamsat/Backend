from typing import List
from app.domain.entities.appotor import AppOtor
from app.domain.repositories.appotor_repository import AppOtorRepository


class AppOtorUseCase:

    def __init__(self, repository: AppOtorRepository):
        self.repository = repository

    def get_all(self) -> List[AppOtor]:
        return self.repository.get_all()

    def get_by_id(self, kdgroup: str, roleid: str) -> AppOtor | None:
        return self.repository.get_by_id(kdgroup, roleid)

    def create(
        self,
        kdgroup: str,
        roleid: str,
        ket: str | None,
        created_by: str | None,
        updated_by: str | None,
    ) -> AppOtor:
        app_otor = AppOtor(
            kdgroup=kdgroup,
            roleid=roleid,
            ket=ket,
            created_by=created_by,
            updated_by=updated_by,
        )
        return self.repository.create(app_otor)

    def update(
        self,
        kdgroup: str,
        roleid: str,
        ket: str | None,
        updated_by: str | None,
    ) -> AppOtor | None:
        app_otor = AppOtor(
            kdgroup=kdgroup,
            roleid=roleid,
            ket=ket,
            updated_by=updated_by,
        )
        return self.repository.update(kdgroup, roleid, app_otor)

    def delete(self, kdgroup: str, roleid: str) -> bool:
        return self.repository.delete(kdgroup, roleid)
