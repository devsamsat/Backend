from typing import List

from app.domain.entities.jnsjr import JnsJr
from app.domain.repositories.jnsjr_repository import JnsJrRepository


class JnsJrUseCase:

    def __init__(self, repository: JnsJrRepository):
        self.repository = repository

    def get_all(self) -> List[JnsJr]:
        return self.repository.get_all()

    def get_by_id(self, jnsjrid: str) -> JnsJr | None:
        return self.repository.get_by_id(jnsjrid)

    def create(
        self,
        jnsjrid: str,
        kodejr: str,
        goljns: str,
        pu: str,
        roda: int,
        keterangan: str | None,
        created_by: str | None,
        updated_by: str | None,
    ) -> JnsJr:
        jns_jr = JnsJr(
            jnsjrid=jnsjrid,
            kodejr=kodejr,
            goljns=goljns,
            pu=pu,
            roda=roda,
            keterangan=keterangan,
            created_by=created_by,
            updated_by=updated_by,
        )
        return self.repository.create(jns_jr)

    def update(
        self,
        jnsjrid: str,
        kodejr: str | None,
        goljns: str | None,
        pu: str | None,
        roda: int | None,
        keterangan: str | None,
        updated_by: str | None,
    ) -> JnsJr | None:
        jns_jr = JnsJr(
            jnsjrid=jnsjrid,
            kodejr=kodejr,
            goljns=goljns,
            pu=pu,
            roda=roda,
            keterangan=keterangan,
            updated_by=updated_by,
        )
        return self.repository.update(jnsjrid, jns_jr)

    def delete(self, jnsjrid: str) -> bool:
        return self.repository.delete(jnsjrid)
