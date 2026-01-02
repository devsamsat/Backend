from typing import List

from app.domain.entities.masterprovinsi import MasterProvinsi
from app.domain.repositories.masterprovinsi_repository import MasterProvinsiRepository


class MasterProvinsiUseCase:

    def __init__(self, repository: MasterProvinsiRepository):
        self.repository = repository

    def get_all(self) -> List[MasterProvinsi]:
        return self.repository.get_all()

    def get_by_id(self, idprovinsi: int) -> MasterProvinsi | None:
        return self.repository.get_by_id(idprovinsi)

    def create(
        self,
        kdprovinsi: str,
        nmprovinsi: str,
        status: str,
        created_by: str | None = None,
        updated_by: str | None = None,
    ) -> MasterProvinsi:
        master_provinsi = MasterProvinsi(
            idprovinsi=None,
            kdprovinsi=kdprovinsi,
            nmprovinsi=nmprovinsi,
            status=status,
            created_by=created_by,
            updated_by=updated_by,
        )
        return self.repository.create(master_provinsi)

    def update(
        self,
        idprovinsi: int,
        kdprovinsi: str | None,
        nmprovinsi: str | None,
        status: str | None,
        updated_by: str | None,
    ) -> MasterProvinsi | None:
        master_provinsi = MasterProvinsi(
            idprovinsi=idprovinsi,
            kdprovinsi=kdprovinsi,
            nmprovinsi=nmprovinsi,
            status=status,
            updated_by=updated_by,
        )
        return self.repository.update(idprovinsi, master_provinsi)

    def delete(self, idprovinsi: int) -> bool:
        return self.repository.delete(idprovinsi)
