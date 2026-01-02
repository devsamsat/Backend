from typing import List

from app.domain.entities.jnsstrurek import JnsStruRek
from app.domain.repositories.jnsstrurek_repository import JnsStruRekRepository


class JnsStruRekUseCase:

    def __init__(self, repository: JnsStruRekRepository):
        self.repository = repository

    def get_all(self) -> List[JnsStruRek]:
        return self.repository.get_all()

    def get_by_id(self, mtglevel: str) -> JnsStruRek | None:
        return self.repository.get_by_id(mtglevel)

    def create(
        self,
        mtglevel: str,
        nmlevel: str,
        keterangan: str,
        created_by: str | None,
        updated_by: str | None,
    ) -> JnsStruRek:
        jns_strurek = JnsStruRek(
            mtglevel=mtglevel,
            nmlevel=nmlevel,
            keterangan=keterangan,
            created_by=created_by,
            updated_by=updated_by,
        )
        return self.repository.create(jns_strurek)

    def update(
        self,
        mtglevel: str,
        nmlevel: str | None,
        keterangan: str | None,
        updated_by: str | None,
    ) -> JnsStruRek | None:
        jns_strurek = JnsStruRek(
            mtglevel=mtglevel,
            nmlevel=nmlevel,
            keterangan=keterangan,
            updated_by=updated_by,
        )
        return self.repository.update(mtglevel, jns_strurek)

    def delete(self, mtglevel: str) -> bool:
        return self.repository.delete(mtglevel)
