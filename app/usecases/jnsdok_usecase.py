from typing import List
from app.domain.entities.jnsdok import JnsDok
from app.domain.repositories.jnsdok_repository import JnsDokRepository


class JnsDokUseCase:

    def __init__(self, repository: JnsDokRepository):
        self.repository = repository

    def get_all(self) -> List[JnsDok]:
        return self.repository.get_all()

    def get_by_id(self, kddok: str) -> JnsDok | None:
        return self.repository.get_by_id(kddok)

    def create(
        self,
        kddok: str,
        namadok: str,
        keterangan: str | None,
        created_by: str | None,
        updated_by: str | None,
    ) -> JnsDok:
        jns_dok = JnsDok(
            kddok=kddok,
            namadok=namadok,
            keterangan=keterangan,
            created_by=created_by,
            updated_by=updated_by,
        )
        return self.repository.create(jns_dok)

    def update(
        self,
        kddok: str,
        namadok: str | None,
        keterangan: str | None,
        updated_by: str | None,
    ) -> JnsDok | None:
        jns_dok = JnsDok(
            kddok=kddok,
            namadok=namadok,
            keterangan=keterangan,
            updated_by=updated_by,
        )
        return self.repository.update(kddok, jns_dok)

    def delete(self, kddok: str) -> bool:
        return self.repository.delete(kddok)
