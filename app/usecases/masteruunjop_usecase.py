from typing import List
from app.domain.entities.masteruunjop import MasterUuNjop
from app.domain.repositories.masteruunjop_repository import MasterUuNjopRepository


class MasterUuNjopUseCase:

    def __init__(self, repository: MasterUuNjopRepository):
        self.repository = repository

    def get_all(self) -> List[MasterUuNjop]:
        return self.repository.get_all()

    def get_by_id(self, iduunjop: int) -> MasterUuNjop | None:
        return self.repository.get_by_id(iduunjop)

    def create(
        self,
        noperkada: str | None,
        isiperkada: str | None,
        tahun: str | None,
        status: str | None,
        keterangan: str | None,
        created_by: str | None,
        updated_by: str | None,
    ) -> MasterUuNjop:
        uu_njop = MasterUuNjop(
            iduunjop=None,
            noperkada=noperkada,
            isiperkada=isiperkada,
            tahun=tahun,
            status=status,
            keterangan=keterangan,
            created_by=created_by,
            updated_by=updated_by,
        )
        return self.repository.create(uu_njop)

    def update(
        self,
        iduunjop: int,
        noperkada: str | None,
        isiperkada: str | None,
        tahun: str | None,
        status: str | None,
        keterangan: str | None,
        updated_by: str | None,
    ) -> MasterUuNjop | None:
        uu_njop = MasterUuNjop(
            iduunjop=iduunjop,
            noperkada=noperkada,
            isiperkada=isiperkada,
            tahun=tahun,
            status=status,
            keterangan=keterangan,
            updated_by=updated_by,
        )
        return self.repository.update(iduunjop, uu_njop)

    def delete(self, iduunjop: int) -> bool:
        return self.repository.delete(iduunjop)
