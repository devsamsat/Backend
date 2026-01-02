from typing import List

from app.domain.entities.masteruunjop import MasterUunJop
from app.domain.repositories.masteruunjop_repository import MasterUunJopRepository


class MasterUunJopUseCase:

    def __init__(self, repository: MasterUunJopRepository):
        self.repository = repository

    def get_all(self) -> List[MasterUunJop]:
        return self.repository.get_all()

    def get_by_id(self, iduunjop: int) -> MasterUunJop | None:
        return self.repository.get_by_id(iduunjop)

    def create(
        self,
        noperkada: str | None = None,
        isiperkada: str | None = None,
        tahun: str | None = None,
        status: str | None = None,
        keterangan: str | None = None,
        created_by: str | None = None,
        updated_by: str | None = None,
    ) -> MasterUunJop:
        master_uun_jop = MasterUunJop(
            iduunjop=None,
            noperkada=noperkada,
            isiperkada=isiperkada,
            tahun=tahun,
            status=status,
            keterangan=keterangan,
            created_by=created_by,
            updated_by=updated_by,
        )
        return self.repository.create(master_uun_jop)

    def update(
        self,
        iduunjop: int,
        noperkada: str | None,
        isiperkada: str | None,
        tahun: str | None,
        status: str | None,
        keterangan: str | None,
        updated_by: str | None,
    ) -> MasterUunJop | None:
        master_uun_jop = MasterUunJop(
            iduunjop=iduunjop,
            noperkada=noperkada,
            isiperkada=isiperkada,
            tahun=tahun,
            status=status,
            keterangan=keterangan,
            updated_by=updated_by,
        )
        return self.repository.update(iduunjop, master_uun_jop)

    def delete(self, iduunjop: int) -> bool:
        return self.repository.delete(iduunjop)
