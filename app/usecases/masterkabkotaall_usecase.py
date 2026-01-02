from typing import List

from app.domain.entities.masterkabkotaall import MasterKabKotaAll
from app.domain.repositories.masterkabkotaall_repository import (
    MasterKabKotaAllRepository,
)


class MasterKabKotaAllUseCase:

    def __init__(self, repository: MasterKabKotaAllRepository):
        self.repository = repository

    def get_all(self) -> List[MasterKabKotaAll]:
        return self.repository.get_all()

    def get_by_id(self, idkabkotaall: int) -> MasterKabKotaAll | None:
        return self.repository.get_by_id(idkabkotaall)

    def create(
        self,
        idprovinsi: int,
        nmkabkota: str,
        status: str,
        kdkabkota: str | None = None,
        created_by: str | None = None,
        updated_by: str | None = None,
    ) -> MasterKabKotaAll:
        master_kabkotaall = MasterKabKotaAll(
            idkabkotaall=None,
            idprovinsi=idprovinsi,
            nmkabkota=nmkabkota,
            status=status,
            kdkabkota=kdkabkota,
            created_by=created_by,
            updated_by=updated_by,
        )
        return self.repository.create(master_kabkotaall)

    def update(
        self,
        idkabkotaall: int,
        idprovinsi: int | None,
        nmkabkota: str | None,
        status: str | None,
        kdkabkota: str | None,
        updated_by: str | None,
    ) -> MasterKabKotaAll | None:
        master_kabkotaall = MasterKabKotaAll(
            idkabkotaall=idkabkotaall,
            idprovinsi=idprovinsi,
            nmkabkota=nmkabkota,
            status=status,
            kdkabkota=kdkabkota,
            updated_by=updated_by,
        )
        return self.repository.update(idkabkotaall, master_kabkotaall)

    def delete(self, idkabkotaall: int) -> bool:
        return self.repository.delete(idkabkotaall)
