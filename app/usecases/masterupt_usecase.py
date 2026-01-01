from typing import List
from app.domain.entities.masterupt import MasterUpt
from app.domain.repositories.masterupt_repository import MasterUptRepository


class MasterUptUseCase:

    def __init__(self, repository: MasterUptRepository):
        self.repository = repository

    def get_all(self) -> List[MasterUpt]:
        return self.repository.get_all()

    def get_by_id(self, idupt: int) -> MasterUpt | None:
        return self.repository.get_by_id(idupt)

    def create(
        self,
        kdupt: str,
        nmupt: str,
        upt_type: str,
        idparent: int | None,
        kdlevel: str | None,
        akroupt: str | None,
        alamat: str | None,
        telepon: str | None,
        idbank: int | None,
        idkabkota: int | None,
        kepala: int | None,
        koordinator: int | None,
        bendahara: int | None,
        norekb: str | None,
        status: str | None,
        created_by: str | None,
        updated_by: str | None,
    ) -> MasterUpt:
        upt = MasterUpt(
            idupt=None,
            kdupt=kdupt,
            nmupt=nmupt,
            upt_type=upt_type,
            idparent=idparent,
            kdlevel=kdlevel,
            akroupt=akroupt,
            alamat=alamat,
            telepon=telepon,
            idbank=idbank,
            idkabkota=idkabkota,
            kepala=kepala,
            koordinator=koordinator,
            bendahara=bendahara,
            norekb=norekb,
            status=status,
            created_by=created_by,
            updated_by=updated_by,
        )
        return self.repository.create(upt)

    def update(
        self,
        idupt: int,
        kdupt: str | None,
        nmupt: str | None,
        upt_type: str | None,
        idparent: int | None,
        kdlevel: str | None,
        akroupt: str | None,
        alamat: str | None,
        telepon: str | None,
        idbank: int | None,
        idkabkota: int | None,
        kepala: int | None,
        koordinator: int | None,
        bendahara: int | None,
        norekb: str | None,
        status: str | None,
        updated_by: str | None,
    ) -> MasterUpt | None:
        upt = MasterUpt(
            idupt=idupt,
            kdupt=kdupt,
            nmupt=nmupt,
            upt_type=upt_type,
            idparent=idparent,
            kdlevel=kdlevel,
            akroupt=akroupt,
            alamat=alamat,
            telepon=telepon,
            idbank=idbank,
            idkabkota=idkabkota,
            kepala=kepala,
            koordinator=koordinator,
            bendahara=bendahara,
            norekb=norekb,
            status=status,
            updated_by=updated_by,
        )
        return self.repository.update(idupt, upt)

    def delete(self, idupt: int) -> bool:
        return self.repository.delete(idupt)
