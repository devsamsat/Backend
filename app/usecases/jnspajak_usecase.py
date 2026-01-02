from typing import List

from app.domain.entities.jnspajak import JnsPajak
from app.domain.repositories.jnspajak_repository import JnsPajakRepository


class JnsPajakUseCase:

    def __init__(self, repository: JnsPajakRepository):
        self.repository = repository

    def get_all(self) -> List[JnsPajak]:
        return self.repository.get_all()

    def get_by_id(self, kdjnspjk: str) -> JnsPajak | None:
        return self.repository.get_by_id(kdjnspjk)

    def create(
        self,
        kdjnspjk: str,
        nmjnspjk: str,
        keterangan: str | None,
        created_by: str | None,
        updated_by: str | None,
    ) -> JnsPajak:
        jns_pajak = JnsPajak(
            kdjnspjk=kdjnspjk,
            nmjnspjk=nmjnspjk,
            keterangan=keterangan,
            created_by=created_by,
            updated_by=updated_by,
        )
        return self.repository.create(jns_pajak)

    def update(
        self,
        kdjnspjk: str,
        nmjnspjk: str | None,
        keterangan: str | None,
        updated_by: str | None,
    ) -> JnsPajak | None:
        jns_pajak = JnsPajak(
            kdjnspjk=kdjnspjk,
            nmjnspjk=nmjnspjk,
            keterangan=keterangan,
            updated_by=updated_by,
        )
        return self.repository.update(kdjnspjk, jns_pajak)

    def delete(self, kdjnspjk: str) -> bool:
        return self.repository.delete(kdjnspjk)
