from typing import List

from app.domain.entities.mastermerk import MasterMerk
from app.domain.repositories.mastermerk_repository import MasterMerkRepository


class MasterMerkUseCase:

    def __init__(self, repository: MasterMerkRepository):
        self.repository = repository

    def get_all(self) -> List[MasterMerk]:
        return self.repository.get_all()

    def get_by_id(self, idmerk: int) -> MasterMerk | None:
        return self.repository.get_by_id(idmerk)

    def create(
        self,
        kdmerk: str | None,
        nmmerk: str,
        keterangan: str | None,
        status: str | None,
        created_by: str | None,
        updated_by: str | None,
    ) -> MasterMerk:
        master_merk = MasterMerk(
            idmerk=None,
            kdmerk=kdmerk,
            nmmerk=nmmerk,
            keterangan=keterangan,
            status=status,
            created_by=created_by,
            updated_by=updated_by,
        )
        return self.repository.create(master_merk)

    def update(
        self,
        idmerk: int,
        kdmerk: str | None,
        nmmerk: str | None,
        keterangan: str | None,
        status: str | None,
        updated_by: str | None,
    ) -> MasterMerk | None:
        master_merk = MasterMerk(
            idmerk=idmerk,
            kdmerk=kdmerk,
            nmmerk=nmmerk,
            keterangan=keterangan,
            status=status,
            updated_by=updated_by,
        )
        return self.repository.update(idmerk, master_merk)

    def delete(self, idmerk: int) -> bool:
        return self.repository.delete(idmerk)
