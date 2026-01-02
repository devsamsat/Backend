from typing import List

from app.domain.entities.jnsumum import JnsUmum
from app.domain.repositories.jnsumum_repository import JnsUmumRepository


class JnsUmumUseCase:

    def __init__(self, repository: JnsUmumRepository):
        self.repository = repository

    def get_all(self) -> List[JnsUmum]:
        return self.repository.get_all()

    def get_by_id(self, kdumum: str) -> JnsUmum | None:
        return self.repository.get_by_id(kdumum)

    def create(
        self,
        kdumum: str,
        nmumum: str,
        keterangan: str,
        status: str | None,
        created_by: str | None,
        updated_by: str | None,
    ) -> JnsUmum:
        jns_umum = JnsUmum(
            kdumum=kdumum,
            nmumum=nmumum,
            keterangan=keterangan,
            status=status,
            created_by=created_by,
            updated_by=updated_by,
        )
        return self.repository.create(jns_umum)

    def update(
        self,
        kdumum: str,
        nmumum: str | None,
        keterangan: str | None,
        status: str | None,
        updated_by: str | None,
    ) -> JnsUmum | None:
        jns_umum = JnsUmum(
            kdumum=kdumum,
            nmumum=nmumum,
            keterangan=keterangan,
            status=status,
            updated_by=updated_by,
        )
        return self.repository.update(kdumum, jns_umum)

    def delete(self, kdumum: str) -> bool:
        return self.repository.delete(kdumum)
