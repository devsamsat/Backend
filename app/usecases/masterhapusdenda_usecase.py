from datetime import date
from decimal import Decimal
from typing import List

from app.domain.entities.masterhapusdenda import MasterHapusDenda
from app.domain.repositories.masterhapusdenda_repository import MasterHapusDendaRepository


class MasterHapusDendaUseCase:

    def __init__(self, repository: MasterHapusDendaRepository):
        self.repository = repository

    def get_all(self) -> List[MasterHapusDenda]:
        return self.repository.get_all()

    def get_by_id(self, idhapusdenda: int) -> MasterHapusDenda | None:
        return self.repository.get_by_id(idhapusdenda)

    def create(
        self,
        jenis: str,
        uraian: str,
        awal: date | None = None,
        akhir: date | None = None,
        nilai: Decimal | None = None,
        satuan: str | None = None,
        ket: str | None = None,
        status: str | None = None,
        created_by: str | None = None,
        updated_by: str | None = None,
    ) -> MasterHapusDenda:
        master_hapus_denda = MasterHapusDenda(
            idhapusdenda=None,
            jenis=jenis,
            uraian=uraian,
            awal=awal,
            akhir=akhir,
            nilai=nilai,
            satuan=satuan,
            ket=ket,
            status=status,
            created_by=created_by,
            updated_by=updated_by,
        )
        return self.repository.create(master_hapus_denda)

    def update(
        self,
        idhapusdenda: int,
        jenis: str | None,
        uraian: str | None,
        awal: date | None,
        akhir: date | None,
        nilai: Decimal | None,
        satuan: str | None,
        ket: str | None,
        status: str | None,
        updated_by: str | None,
    ) -> MasterHapusDenda | None:
        master_hapus_denda = MasterHapusDenda(
            idhapusdenda=idhapusdenda,
            jenis=jenis,
            uraian=uraian,
            awal=awal,
            akhir=akhir,
            nilai=nilai,
            satuan=satuan,
            ket=ket,
            status=status,
            updated_by=updated_by,
        )
        return self.repository.update(idhapusdenda, master_hapus_denda)

    def delete(self, idhapusdenda: int) -> bool:
        return self.repository.delete(idhapusdenda)
