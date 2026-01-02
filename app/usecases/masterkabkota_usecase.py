from typing import List

from app.domain.entities.masterkabkota import MasterKabKota
from app.domain.repositories.masterkabkota_repository import MasterKabKotaRepository


class MasterKabKotaUseCase:

    def __init__(self, repository: MasterKabKotaRepository):
        self.repository = repository

    def get_all(self) -> List[MasterKabKota]:
        return self.repository.get_all()

    def get_by_id(self, idkabkota: int) -> MasterKabKota | None:
        return self.repository.get_by_id(idkabkota)

    def create(
        self,
        idprovinsi: int,
        nmkabkota: str,
        akronim: str,
        ibukota: str,
        status: str,
        bpkbid: str,
        kdkabkota: str | None = None,
        created_by: str | None = None,
        updated_by: str | None = None,
    ) -> MasterKabKota:
        master_kabkota = MasterKabKota(
            idkabkota=None,
            idprovinsi=idprovinsi,
            nmkabkota=nmkabkota,
            akronim=akronim,
            ibukota=ibukota,
            status=status,
            bpkbid=bpkbid,
            kdkabkota=kdkabkota,
            created_by=created_by,
            updated_by=updated_by,
        )
        return self.repository.create(master_kabkota)

    def update(
        self,
        idkabkota: int,
        idprovinsi: int | None,
        nmkabkota: str | None,
        akronim: str | None,
        ibukota: str | None,
        status: str | None,
        bpkbid: str | None,
        kdkabkota: str | None,
        updated_by: str | None,
    ) -> MasterKabKota | None:
        master_kabkota = MasterKabKota(
            idkabkota=idkabkota,
            idprovinsi=idprovinsi,
            nmkabkota=nmkabkota,
            akronim=akronim,
            ibukota=ibukota,
            status=status,
            bpkbid=bpkbid,
            kdkabkota=kdkabkota,
            updated_by=updated_by,
        )
        return self.repository.update(idkabkota, master_kabkota)

    def delete(self, idkabkota: int) -> bool:
        return self.repository.delete(idkabkota)
