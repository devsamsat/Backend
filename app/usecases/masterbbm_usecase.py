from typing import List

from app.domain.entities.masterbbm import MasterBbm
from app.domain.repositories.masterbbm_repository import MasterBbmRepository


class MasterBbmUseCase:

    def __init__(self, repository: MasterBbmRepository):
        self.repository = repository

    def get_all(self) -> List[MasterBbm]:
        return self.repository.get_all()

    def get_by_id(self, kodebbm: str) -> MasterBbm | None:
        return self.repository.get_by_id(kodebbm)

    def create(
        self,
        kodebbm: str,
        namabbm: str,
        keterangan: str | None = None,
        created_by: str | None = None,
        updated_by: str | None = None,
    ) -> MasterBbm:
        master_bbm = MasterBbm(
            kodebbm=kodebbm,
            namabbm=namabbm,
            keterangan=keterangan,
            created_by=created_by,
            updated_by=updated_by,
        )
        return self.repository.create(master_bbm)

    def update(
        self,
        kodebbm: str,
        namabbm: str | None,
        keterangan: str | None,
        updated_by: str | None,
    ) -> MasterBbm | None:
        master_bbm = MasterBbm(
            kodebbm=kodebbm,
            namabbm=namabbm,
            keterangan=keterangan,
            updated_by=updated_by,
        )
        return self.repository.update(kodebbm, master_bbm)

    def delete(self, kodebbm: str) -> bool:
        return self.repository.delete(kodebbm)
