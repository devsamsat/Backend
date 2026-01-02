from datetime import date
from typing import List

from app.domain.entities.transsts import TransSts
from app.domain.repositories.transsts_repository import TransStsRepository


class TransStsUseCase:

    def __init__(self, repository: TransStsRepository):
        self.repository = repository

    def get_all(self) -> List[TransSts]:
        return self.repository.get_all()

    def get_by_id(self, idsts: int) -> TransSts | None:
        return self.repository.get_by_id(idsts)

    def create(
        self,
        idupt: int,
        idbend: int,
        nosts: str,
        keterangan: str,
        statbayar: str,
        setorandari: str | None = None,
        tglsts: date | None = None,
        ntpd: str | None = None,
        tglntpd: date | None = None,
        statsts: int | None = None,
        created_by: str | None = None,
        updated_by: str | None = None,
    ) -> TransSts:
        trans_sts = TransSts(
            idsts=None,
            idupt=idupt,
            idbend=idbend,
            nosts=nosts,
            keterangan=keterangan,
            statbayar=statbayar,
            setorandari=setorandari,
            tglsts=tglsts,
            ntpd=ntpd,
            tglntpd=tglntpd,
            statsts=statsts,
            created_by=created_by,
            updated_by=updated_by,
        )
        return self.repository.create(trans_sts)

    def update(
        self,
        idsts: int,
        idupt: int | None,
        idbend: int | None,
        nosts: str | None,
        keterangan: str | None,
        statbayar: str | None,
        setorandari: str | None,
        tglsts: date | None,
        ntpd: str | None,
        tglntpd: date | None,
        statsts: int | None,
        updated_by: str | None,
    ) -> TransSts | None:
        trans_sts = TransSts(
            idsts=idsts,
            idupt=idupt,
            idbend=idbend,
            nosts=nosts,
            keterangan=keterangan,
            statbayar=statbayar,
            setorandari=setorandari,
            tglsts=tglsts,
            ntpd=ntpd,
            tglntpd=tglntpd,
            statsts=statsts,
            updated_by=updated_by,
        )
        return self.repository.update(idsts, trans_sts)

    def delete(self, idsts: int) -> bool:
        return self.repository.delete(idsts)
