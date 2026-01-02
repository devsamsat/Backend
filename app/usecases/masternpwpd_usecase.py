from datetime import date
from typing import List

from app.domain.entities.masternpwpd import MasterNpwpd
from app.domain.repositories.masternpwpd_repository import MasterNpwpdRepository


class MasterNpwpdUseCase:

    def __init__(self, repository: MasterNpwpdRepository):
        self.repository = repository

    def get_all(self) -> List[MasterNpwpd]:
        return self.repository.get_all()

    def get_by_id(self, idnpwpd: int) -> MasterNpwpd | None:
        return self.repository.get_by_id(idnpwpd)

    def create(
        self,
        statnpwpd: str | None,
        npwpd: str,
        idbadan: int | None,
        idktp: int | None,
        tgldaftar: date | None,
        nib: str | None,
        namabadan: str | None,
        alamat: str | None,
        status: str | None,
        ket: str | None,
        created_by: str | None,
        updated_by: str | None,
    ) -> MasterNpwpd:
        master_npwpd = MasterNpwpd(
            idnpwpd=None,
            statnpwpd=statnpwpd,
            npwpd=npwpd,
            idbadan=idbadan,
            idktp=idktp,
            tgldaftar=tgldaftar,
            nib=nib,
            namabadan=namabadan,
            alamat=alamat,
            status=status,
            ket=ket,
            created_by=created_by,
            updated_by=updated_by,
        )
        return self.repository.create(master_npwpd)

    def update(
        self,
        idnpwpd: int,
        statnpwpd: str | None,
        npwpd: str | None,
        idbadan: int | None,
        idktp: int | None,
        tgldaftar: date | None,
        nib: str | None,
        namabadan: str | None,
        alamat: str | None,
        status: str | None,
        ket: str | None,
        updated_by: str | None,
    ) -> MasterNpwpd | None:
        master_npwpd = MasterNpwpd(
            idnpwpd=idnpwpd,
            statnpwpd=statnpwpd,
            npwpd=npwpd,
            idbadan=idbadan,
            idktp=idktp,
            tgldaftar=tgldaftar,
            nib=nib,
            namabadan=namabadan,
            alamat=alamat,
            status=status,
            ket=ket,
            updated_by=updated_by,
        )
        return self.repository.update(idnpwpd, master_npwpd)

    def delete(self, idnpwpd: int) -> bool:
        return self.repository.delete(idnpwpd)
