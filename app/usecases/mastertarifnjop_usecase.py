from decimal import Decimal
from typing import List

from app.domain.entities.mastertarifnjop import MasterTarifNjop
from app.domain.repositories.mastertarifnjop_repository import MasterTarifNjopRepository


class MasterTarifNjopUseCase:

    def __init__(self, repository: MasterTarifNjopRepository):
        self.repository = repository

    def get_all(self) -> List[MasterTarifNjop]:
        return self.repository.get_all()

    def get_by_id(self, idtarifnjop: int) -> MasterTarifNjop | None:
        return self.repository.get_by_id(idtarifnjop)

    def create(
        self,
        iduunjop: int,
        idrekd: int | None = None,
        kdjnstarif: str | None = None,
        namatarif: str | None = None,
        idmerk: int | None = None,
        tipe: str | None = None,
        silinder: str | None = None,
        tahun: str | None = None,
        kodebbm: str | None = None,
        njop: Decimal | None = None,
        status: str | None = None,
        created_by: str | None = None,
        updated_by: str | None = None,
    ) -> MasterTarifNjop:
        master_tarif_njop = MasterTarifNjop(
            idtarifnjop=None,
            iduunjop=iduunjop,
            idrekd=idrekd,
            kdjnstarif=kdjnstarif,
            namatarif=namatarif,
            idmerk=idmerk,
            tipe=tipe,
            silinder=silinder,
            tahun=tahun,
            kodebbm=kodebbm,
            njop=njop,
            status=status,
            created_by=created_by,
            updated_by=updated_by,
        )
        return self.repository.create(master_tarif_njop)

    def update(
        self,
        idtarifnjop: int,
        iduunjop: int | None,
        idrekd: int | None,
        kdjnstarif: str | None,
        namatarif: str | None,
        idmerk: int | None,
        tipe: str | None,
        silinder: str | None,
        tahun: str | None,
        kodebbm: str | None,
        njop: Decimal | None,
        status: str | None,
        updated_by: str | None,
    ) -> MasterTarifNjop | None:
        master_tarif_njop = MasterTarifNjop(
            idtarifnjop=idtarifnjop,
            iduunjop=iduunjop,
            idrekd=idrekd,
            kdjnstarif=kdjnstarif,
            namatarif=namatarif,
            idmerk=idmerk,
            tipe=tipe,
            silinder=silinder,
            tahun=tahun,
            kodebbm=kodebbm,
            njop=njop,
            status=status,
            updated_by=updated_by,
        )
        return self.repository.update(idtarifnjop, master_tarif_njop)

    def delete(self, idtarifnjop: int) -> bool:
        return self.repository.delete(idtarifnjop)
