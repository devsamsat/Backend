from datetime import date
from typing import List

from app.domain.entities.masterbadan import MasterBadan
from app.domain.repositories.masterbadan_repository import MasterBadanRepository


class MasterBadanUseCase:

    def __init__(self, repository: MasterBadanRepository):
        self.repository = repository

    def get_all(self) -> List[MasterBadan]:
        return self.repository.get_all()

    def get_by_id(self, idbadan: int) -> MasterBadan | None:
        return self.repository.get_by_id(idbadan)

    def create(
        self,
        namabadan: str,
        nohp: str,
        alamat: str,
        nib: str | None = None,
        idktp: int | None = None,
        tgldaftar: date | None = None,
        idprovinsi: int | None = None,
        idkabkokta: int | None = None,
        ket: str | None = None,
        created_by: str | None = None,
        updated_by: str | None = None,
    ) -> MasterBadan:
        master_badan = MasterBadan(
            idbadan=None,
            namabadan=namabadan,
            nohp=nohp,
            alamat=alamat,
            nib=nib,
            idktp=idktp,
            tgldaftar=tgldaftar,
            idprovinsi=idprovinsi,
            idkabkokta=idkabkokta,
            ket=ket,
            created_by=created_by,
            updated_by=updated_by,
        )
        return self.repository.create(master_badan)

    def update(
        self,
        idbadan: int,
        namabadan: str | None,
        nohp: str | None,
        alamat: str | None,
        nib: str | None,
        idktp: int | None,
        tgldaftar: date | None,
        idprovinsi: int | None,
        idkabkokta: int | None,
        ket: str | None,
        updated_by: str | None,
    ) -> MasterBadan | None:
        master_badan = MasterBadan(
            idbadan=idbadan,
            namabadan=namabadan,
            nohp=nohp,
            alamat=alamat,
            nib=nib,
            idktp=idktp,
            tgldaftar=tgldaftar,
            idprovinsi=idprovinsi,
            idkabkokta=idkabkokta,
            ket=ket,
            updated_by=updated_by,
        )
        return self.repository.update(idbadan, master_badan)

    def delete(self, idbadan: int) -> bool:
        return self.repository.delete(idbadan)
