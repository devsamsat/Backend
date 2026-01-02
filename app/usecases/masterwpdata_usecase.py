from datetime import date
from typing import List

from app.domain.entities.masterwpdata import MasterWpData
from app.domain.repositories.masterwpdata_repository import MasterWpDataRepository


class MasterWpDataUseCase:

    def __init__(self, repository: MasterWpDataRepository):
        self.repository = repository

    def get_all(self) -> List[MasterWpData]:
        return self.repository.get_all()

    def get_by_id(self, idwpdata: int) -> MasterWpData | None:
        return self.repository.get_by_id(idwpdata)

    def create(
        self,
        idjnsd: int,
        idwp: int,
        tglpendataan: date | None = None,
        created_by: str | None = None,
        updated_by: str | None = None,
    ) -> MasterWpData:
        master_wpdata = MasterWpData(
            idwpdata=None,
            idjnsd=idjnsd,
            idwp=idwp,
            tglpendataan=tglpendataan,
            created_by=created_by,
            updated_by=updated_by,
        )
        return self.repository.create(master_wpdata)

    def update(
        self,
        idwpdata: int,
        idjnsd: int | None,
        idwp: int | None,
        tglpendataan: date | None,
        updated_by: str | None,
    ) -> MasterWpData | None:
        master_wpdata = MasterWpData(
            idwpdata=idwpdata,
            idjnsd=idjnsd,
            idwp=idwp,
            tglpendataan=tglpendataan,
            updated_by=updated_by,
        )
        return self.repository.update(idwpdata, master_wpdata)

    def delete(self, idwpdata: int) -> bool:
        return self.repository.delete(idwpdata)
