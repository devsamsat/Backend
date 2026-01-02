from datetime import date
from typing import List

from app.domain.entities.transwpdata import TransWpData
from app.domain.repositories.transwpdata_repository import TransWpDataRepository


class TransWpDataUseCase:

    def __init__(self, repository: TransWpDataRepository):
        self.repository = repository

    def get_all(self) -> List[TransWpData]:
        return self.repository.get_all()

    def get_by_id(self, idtwpdata: int) -> TransWpData | None:
        return self.repository.get_by_id(idtwpdata)

    def create(
        self,
        idnpwpd: int,
        kdflow: str | None = None,
        tgldaftar: date | None = None,
        created_by: str | None = None,
        updated_by: str | None = None,
    ) -> TransWpData:
        trans_wpdata = TransWpData(
            idtwpdata=None,
            idnpwpd=idnpwpd,
            kdflow=kdflow,
            tgldaftar=tgldaftar,
            created_by=created_by,
            updated_by=updated_by,
        )
        return self.repository.create(trans_wpdata)

    def update(
        self,
        idtwpdata: int,
        idnpwpd: int | None,
        kdflow: str | None,
        tgldaftar: date | None,
        updated_by: str | None,
    ) -> TransWpData | None:
        trans_wpdata = TransWpData(
            idtwpdata=idtwpdata,
            idnpwpd=idnpwpd,
            kdflow=kdflow,
            tgldaftar=tgldaftar,
            updated_by=updated_by,
        )
        return self.repository.update(idtwpdata, trans_wpdata)

    def delete(self, idtwpdata: int) -> bool:
        return self.repository.delete(idtwpdata)
