from typing import List

from app.domain.entities.masterkecamatan import MasterKecamatan
from app.domain.repositories.masterkecamatan_repository import MasterKecamatanRepository


class MasterKecamatanUseCase:

    def __init__(self, repository: MasterKecamatanRepository):
        self.repository = repository

    def get_all(self) -> List[MasterKecamatan]:
        return self.repository.get_all()

    def get_by_id(self, idkecamatan: int) -> MasterKecamatan | None:
        return self.repository.get_by_id(idkecamatan)

    def create(
        self,
        idkabkota: int,
        nmkecamatan: str,
        alamat: str,
        telepon: str,
        status: str,
        kdkecamatan: str | None = None,
        fax: str | None = None,
        created_by: str | None = None,
        updated_by: str | None = None,
    ) -> MasterKecamatan:
        master_kecamatan = MasterKecamatan(
            idkecamatan=None,
            idkabkota=idkabkota,
            nmkecamatan=nmkecamatan,
            alamat=alamat,
            telepon=telepon,
            status=status,
            kdkecamatan=kdkecamatan,
            fax=fax,
            created_by=created_by,
            updated_by=updated_by,
        )
        return self.repository.create(master_kecamatan)

    def update(
        self,
        idkecamatan: int,
        idkabkota: int | None,
        nmkecamatan: str | None,
        alamat: str | None,
        telepon: str | None,
        status: str | None,
        kdkecamatan: str | None,
        fax: str | None,
        updated_by: str | None,
    ) -> MasterKecamatan | None:
        master_kecamatan = MasterKecamatan(
            idkecamatan=idkecamatan,
            idkabkota=idkabkota,
            nmkecamatan=nmkecamatan,
            alamat=alamat,
            telepon=telepon,
            status=status,
            kdkecamatan=kdkecamatan,
            fax=fax,
            updated_by=updated_by,
        )
        return self.repository.update(idkecamatan, master_kecamatan)

    def delete(self, idkecamatan: int) -> bool:
        return self.repository.delete(idkecamatan)
