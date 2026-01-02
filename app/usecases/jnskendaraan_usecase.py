from typing import List

from app.domain.entities.jnskendaraan import JnsKendaraan
from app.domain.repositories.jnskendaraan_repository import JnsKendaraanRepository


class JnsKendaraanUseCase:

    def __init__(self, repository: JnsKendaraanRepository):
        self.repository = repository

    def get_all(self) -> List[JnsKendaraan]:
        return self.repository.get_all()

    def get_by_id(self, jnskendid: str) -> JnsKendaraan | None:
        return self.repository.get_by_id(jnskendid)

    def create(
        self,
        jnskendid: str,
        jnskend: str,
        katid: str,
        jnsjrid: str | None,
        golpjr: int | None,
        golujr: int | None,
        created_by: str | None,
        updated_by: str | None,
    ) -> JnsKendaraan:
        jns_kendaraan = JnsKendaraan(
            jnskendid=jnskendid,
            jnskend=jnskend,
            katid=katid,
            jnsjrid=jnsjrid,
            golpjr=golpjr,
            golujr=golujr,
            created_by=created_by,
            updated_by=updated_by,
        )
        return self.repository.create(jns_kendaraan)

    def update(
        self,
        jnskendid: str,
        jnskend: str | None,
        katid: str | None,
        jnsjrid: str | None,
        golpjr: int | None,
        golujr: int | None,
        updated_by: str | None,
    ) -> JnsKendaraan | None:
        jns_kendaraan = JnsKendaraan(
            jnskendid=jnskendid,
            jnskend=jnskend,
            katid=katid,
            jnsjrid=jnsjrid,
            golpjr=golpjr,
            golujr=golujr,
            updated_by=updated_by,
        )
        return self.repository.update(jnskendid, jns_kendaraan)

    def delete(self, jnskendid: str) -> bool:
        return self.repository.delete(jnskendid)
