from decimal import Decimal
from typing import List

from app.domain.entities.mastertarif import MasterTarif
from app.domain.repositories.mastertarif_repository import MasterTarifRepository


class MasterTarifUseCase:

    def __init__(self, repository: MasterTarifRepository):
        self.repository = repository

    def get_all(self) -> List[MasterTarif]:
        return self.repository.get_all()

    def get_by_id(self, idtarif: int) -> MasterTarif | None:
        return self.repository.get_by_id(idtarif)

    def create(
        self,
        kdjnspjk: str,
        jnskendid: str | None = None,
        satuan: str | None = None,
        awal: Decimal | None = None,
        akhir: Decimal | None = None,
        keterangan: str | None = None,
        kdflow: str | None = None,
        kdplat: str | None = None,
        statumum: str | None = None,
        tarif: Decimal | None = None,
        created_by: str | None = None,
        updated_by: str | None = None,
    ) -> MasterTarif:
        master_tarif = MasterTarif(
            idtarif=None,
            kdjnspjk=kdjnspjk,
            jnskendid=jnskendid,
            satuan=satuan,
            awal=awal,
            akhir=akhir,
            keterangan=keterangan,
            kdflow=kdflow,
            kdplat=kdplat,
            statumum=statumum,
            tarif=tarif,
            created_by=created_by,
            updated_by=updated_by,
        )
        return self.repository.create(master_tarif)

    def update(
        self,
        idtarif: int,
        kdjnspjk: str | None,
        jnskendid: str | None,
        satuan: str | None,
        awal: Decimal | None,
        akhir: Decimal | None,
        keterangan: str | None,
        kdflow: str | None,
        kdplat: str | None,
        statumum: str | None,
        tarif: Decimal | None,
        updated_by: str | None,
    ) -> MasterTarif | None:
        master_tarif = MasterTarif(
            idtarif=idtarif,
            kdjnspjk=kdjnspjk,
            jnskendid=jnskendid,
            satuan=satuan,
            awal=awal,
            akhir=akhir,
            keterangan=keterangan,
            kdflow=kdflow,
            kdplat=kdplat,
            statumum=statumum,
            tarif=tarif,
            updated_by=updated_by,
        )
        return self.repository.update(idtarif, master_tarif)

    def delete(self, idtarif: int) -> bool:
        return self.repository.delete(idtarif)
