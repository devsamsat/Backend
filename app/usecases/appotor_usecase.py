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

    def create(self, appotor: AppOtor) -> AppOtor:
        return self.repository.create(appotor)

    def update(self, kdgroup: str, roleid: str, appotor: AppOtor) -> AppOtor | None:
        return self.repository.update(kdgroup, roleid, appotor)

    def delete(self, kdgroup: str, roleid: str) -> bool:
        return self.repository.delete(kdgroup, roleid)
