from typing import List

from app.domain.entities.masterjabttd import MasterJabTtd
from app.domain.repositories.masterjabttd_repository import MasterJabTtdRepository


class MasterJabTtdUseCase:

    def __init__(self, repository: MasterJabTtdRepository):
        self.repository = repository

    def get_all(self) -> List[MasterJabTtd]:
        return self.repository.get_all()

    def get_by_id(self, idjabttd: int) -> MasterJabTtd | None:
        return self.repository.get_by_id(idjabttd)

    def create(
        self,
        idpegawai: int,
        kddok: str,
        jabatan: str | None = None,
        ket: str | None = None,
        status: str | None = None,
        created_by: str | None = None,
        updated_by: str | None = None,
    ) -> MasterJabTtd:
        master_jab_ttd = MasterJabTtd(
            idjabttd=None,
            idpegawai=idpegawai,
            kddok=kddok,
            jabatan=jabatan,
            ket=ket,
            status=status,
            created_by=created_by,
            updated_by=updated_by,
        )
        return self.repository.create(master_jab_ttd)

    def update(
        self,
        idjabttd: int,
        idpegawai: int | None,
        kddok: str | None,
        jabatan: str | None,
        ket: str | None,
        status: str | None,
        updated_by: str | None,
    ) -> MasterJabTtd | None:
        master_jab_ttd = MasterJabTtd(
            idjabttd=idjabttd,
            idpegawai=idpegawai,
            kddok=kddok,
            jabatan=jabatan,
            ket=ket,
            status=status,
            updated_by=updated_by,
        )
        return self.repository.update(idjabttd, master_jab_ttd)

    def delete(self, idjabttd: int) -> bool:
        return self.repository.delete(idjabttd)
