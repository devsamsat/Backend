from datetime import date
from typing import List

from app.domain.entities.masterlibur import MasterLibur
from app.domain.repositories.masterlibur_repository import MasterLiburRepository


class MasterLiburUseCase:

    def __init__(self, repository: MasterLiburRepository):
        self.repository = repository

    def get_all(self) -> List[MasterLibur]:
        return self.repository.get_all()

    def get_by_id(self, idlibur: int) -> MasterLibur | None:
        return self.repository.get_by_id(idlibur)

    def create(
        self,
        idkabkota: int,
        level: str,
        tanggal: date | None,
        namalibur: str | None,
        keterangan: str | None,
        created_by: str | None,
        updated_by: str | None,
    ) -> MasterLibur:
        master_libur = MasterLibur(
            idlibur=None,
            idkabkota=idkabkota,
            level=level,
            tanggal=tanggal,
            namalibur=namalibur,
            keterangan=keterangan,
            created_by=created_by,
            updated_by=updated_by,
        )
        return self.repository.create(master_libur)

    def update(
        self,
        idlibur: int,
        idkabkota: int | None,
        level: str | None,
        tanggal: date | None,
        namalibur: str | None,
        keterangan: str | None,
        updated_by: str | None,
    ) -> MasterLibur | None:
        master_libur = MasterLibur(
            idlibur=idlibur,
            idkabkota=idkabkota,
            level=level,
            tanggal=tanggal,
            namalibur=namalibur,
            keterangan=keterangan,
            updated_by=updated_by,
        )
        return self.repository.update(idlibur, master_libur)

    def delete(self, idlibur: int) -> bool:
        return self.repository.delete(idlibur)
