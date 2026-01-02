from typing import List

from app.domain.entities.transwpdataantri import TransWpDataAntri
from app.domain.repositories.transwpdataantri_repository import TransWpDataAntriRepository


class TransWpDataAntriUseCase:

    def __init__(self, repository: TransWpDataAntriRepository):
        self.repository = repository

    def get_all(self) -> List[TransWpDataAntri]:
        return self.repository.get_all()

    def get_by_id(self, idantri: int) -> TransWpDataAntri | None:
        return self.repository.get_by_id(idantri)

    def create(
        self,
        idtwpdata: int,
        noantri: str,
        idktp: int | None = None,
        statantri: str | None = None,
        ket: str | None = None,
        tglantri: str | None = None,
        created_by: str | None = None,
        updated_by: str | None = None,
    ) -> TransWpDataAntri:
        trans_wpdataantri = TransWpDataAntri(
            idantri=None,
            idtwpdata=idtwpdata,
            noantri=noantri,
            idktp=idktp,
            statantri=statantri,
            ket=ket,
            tglantri=tglantri,
            created_by=created_by,
            updated_by=updated_by,
        )
        return self.repository.create(trans_wpdataantri)

    def update(
        self,
        idantri: int,
        idtwpdata: int | None,
        noantri: str | None,
        idktp: int | None,
        statantri: str | None,
        ket: str | None,
        tglantri: str | None,
        updated_by: str | None,
    ) -> TransWpDataAntri | None:
        trans_wpdataantri = TransWpDataAntri(
            idantri=idantri,
            idtwpdata=idtwpdata,
            noantri=noantri,
            idktp=idktp,
            statantri=statantri,
            ket=ket,
            tglantri=tglantri,
            updated_by=updated_by,
        )
        return self.repository.update(idantri, trans_wpdataantri)

    def delete(self, idantri: int) -> bool:
        return self.repository.delete(idantri)
