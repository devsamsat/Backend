from typing import List
from app.domain.entities.jnsguna import JnsGuna
from app.domain.repositories.jnsguna_repository import JnsGunaRepository


class JnsGunaUseCase:

    def __init__(self, repository: JnsGunaRepository):
        self.repository = repository

    def get_all(self) -> List[JnsGuna]:
        return self.repository.get_all()

    def get_by_id(self, kdguna: str) -> JnsGuna | None:
        return self.repository.get_by_id(kdguna)

    def create(
        self,
        kdguna: str,
        guna: str,
        gunaplat: str | None,
        progresif: float | None,
        groupbpkb: str,
        created_by: str | None,
        updated_by: str | None,
    ) -> JnsGuna:
        jns_guna = JnsGuna(
            kdguna=kdguna,
            guna=guna,
            gunaplat=gunaplat,
            progresif=progresif,
            groupbpkb=groupbpkb,
            created_by=created_by,
            updated_by=updated_by,
        )
        return self.repository.create(jns_guna)

    def update(
        self,
        kdguna: str,
        guna: str | None,
        gunaplat: str | None,
        progresif: float | None,
        groupbpkb: str | None,
        updated_by: str | None,
    ) -> JnsGuna | None:
        jns_guna = JnsGuna(
            kdguna=kdguna,
            guna=guna,
            gunaplat=gunaplat,
            progresif=progresif,
            groupbpkb=groupbpkb,
            updated_by=updated_by,
        )
        return self.repository.update(kdguna, jns_guna)

    def delete(self, kdguna: str) -> bool:
        return self.repository.delete(kdguna)
