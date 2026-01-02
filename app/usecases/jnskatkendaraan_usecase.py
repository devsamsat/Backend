from typing import List

from app.domain.entities.jnskatkendaraan import JnsKatKendaraan
from app.domain.repositories.jnskatkendaraan_repository import JnsKatKendaraanRepository


class JnsKatKendaraanUseCase:

    def __init__(self, repository: JnsKatKendaraanRepository):
        self.repository = repository

    def get_all(self) -> List[JnsKatKendaraan]:
        return self.repository.get_all()

    def get_by_id(self, katid: str) -> JnsKatKendaraan | None:
        return self.repository.get_by_id(katid)

    def create(
        self,
        katid: str,
        kendaraan: str,
        jenisbpkb: str,
        status: str | None,
        created_by: str | None,
        updated_by: str | None,
    ) -> JnsKatKendaraan:
        jns_katkendaraan = JnsKatKendaraan(
            katid=katid,
            kendaraan=kendaraan,
            jenisbpkb=jenisbpkb,
            status=status,
            created_by=created_by,
            updated_by=updated_by,
        )
        return self.repository.create(jns_katkendaraan)

    def update(
        self,
        katid: str,
        kendaraan: str | None,
        jenisbpkb: str | None,
        status: str | None,
        updated_by: str | None,
    ) -> JnsKatKendaraan | None:
        jns_katkendaraan = JnsKatKendaraan(
            katid=katid,
            kendaraan=kendaraan,
            jenisbpkb=jenisbpkb,
            status=status,
            updated_by=updated_by,
        )
        return self.repository.update(katid, jns_katkendaraan)

    def delete(self, katid: str) -> bool:
        return self.repository.delete(katid)
