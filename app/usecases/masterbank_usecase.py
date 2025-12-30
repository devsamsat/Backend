from typing import List

from app.domain.entities.masterbank import MasterBank
from app.domain.repositories.masterbank_repository import MasterBankRepository


class MasterBankUseCase:

    def __init__(self, repository: MasterBankRepository):
        self.repository = repository

    def get_all(self) -> List[MasterBank]:
        return self.repository.get_all()

    def get_by_id(self, idbank: int) -> MasterBank | None:
        return self.repository.get_by_id(idbank)

    def create(
        self,
        kodebank: str,
        namabank: str,
        akronimbank: str | None = None,
        cabangbank: str | None = None,
        alamatbank: str | None = None,
        status: str | None = None,
        created_by: str | None = None,
        updated_by: str | None = None,
    ) -> MasterBank:
        master_bank = MasterBank(
            idbank=None,
            kodebank=kodebank,
            namabank=namabank,
            akronimbank=akronimbank,
            cabangbank=cabangbank,
            alamatbank=alamatbank,
            status=status,
            created_by=created_by,
            updated_by=updated_by,
        )
        return self.repository.create(master_bank)

    def update(
        self,
        idbank: int,
        kodebank: str | None,
        namabank: str | None,
        akronimbank: str | None,
        cabangbank: str | None,
        alamatbank: str | None,
        status: str | None,
        updated_by: str | None,
    ) -> MasterBank | None:
        master_bank = MasterBank(
            idbank=idbank,
            kodebank=kodebank,
            namabank=namabank,
            akronimbank=akronimbank,
            cabangbank=cabangbank,
            alamatbank=alamatbank,
            status=status,
            updated_by=updated_by,
        )
        return self.repository.update(idbank, master_bank)

    def delete(self, idbank: int) -> bool:
        return self.repository.delete(idbank)
