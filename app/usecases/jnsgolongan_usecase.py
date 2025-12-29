from typing import List
from app.domain.entities.jnsgolongan import JnsGolongan
from app.domain.repositories.jnsgolongan_repository import JnsGolonganRepository


class JnsGolonganUseCase:

    def __init__(self, repository: JnsGolonganRepository):
        self.repository = repository

    def get_all(self) -> List[JnsGolongan]:
        return self.repository.get_all()

    def get_by_id(self, jnsgolid: str) -> JnsGolongan | None:
        return self.repository.get_by_id(jnsgolid)

    def create(
        self,
        jnsgolid: str,
        golongan: str,
        katid: str | None,
        jnskendid: str | None,
        viewall: str | None,
        status: str | None,
        created_by: str | None,
        updated_by: str | None,
    ) -> JnsGolongan:
        jns_golongan = JnsGolongan(
            jnsgolid=jnsgolid,
            golongan=golongan,
            katid=katid,
            jnskendid=jnskendid,
            viewall=viewall,
            status=status,
            created_by=created_by,
            updated_by=updated_by,
        )
        return self.repository.create(jns_golongan)

    def update(
        self,
        jnsgolid: str,
        golongan: str | None,
        katid: str | None,
        jnskendid: str | None,
        viewall: str | None,
        status: str | None,
        updated_by: str | None,
    ) -> JnsGolongan | None:
        jns_golongan = JnsGolongan(
            jnsgolid=jnsgolid,
            golongan=golongan,
            katid=katid,
            jnskendid=jnskendid,
            viewall=viewall,
            status=status,
            updated_by=updated_by,
        )
        return self.repository.update(jnsgolid, jns_golongan)

    def delete(self, jnsgolid: str) -> bool:
        return self.repository.delete(jnsgolid)
