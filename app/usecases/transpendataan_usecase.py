from datetime import date
from decimal import Decimal
from typing import List

from app.domain.entities.transpendataan import TransPendataan
from app.domain.repositories.transpendataan_repository import TransPendataanRepository


class TransPendataanUseCase:

    def __init__(self, repository: TransPendataanRepository):
        self.repository = repository

    def get_all(self) -> List[TransPendataan]:
        return self.repository.get_all()

    def get_by_id(self, idpendataan: int) -> TransPendataan | None:
        return self.repository.get_by_id(idpendataan)

    def create(
        self,
        spt: str,
        idwpdata: int,
        uruttgl: int,
        tarifpjk: Decimal,
        idupt: int,
        status: str,
        tglpendataan: date | None = None,
        masaawal: date | None = None,
        masaakhir: date | None = None,
        jmlomzetawal: Decimal | None = None,
        kdflow: str | None = None,
        created_by: str | None = None,
        updated_by: str | None = None,
    ) -> TransPendataan:
        trans_pendataan = TransPendataan(
            idpendataan=None,
            spt=spt,
            idwpdata=idwpdata,
            uruttgl=uruttgl,
            tarifpjk=tarifpjk,
            idupt=idupt,
            status=status,
            tglpendataan=tglpendataan,
            masaawal=masaawal,
            masaakhir=masaakhir,
            jmlomzetawal=jmlomzetawal,
            kdflow=kdflow,
            created_by=created_by,
            updated_by=updated_by,
        )
        return self.repository.create(trans_pendataan)

    def update(
        self,
        idpendataan: int,
        spt: str | None,
        idwpdata: int | None,
        uruttgl: int | None,
        tarifpjk: Decimal | None,
        idupt: int | None,
        status: str | None,
        tglpendataan: date | None,
        masaawal: date | None,
        masaakhir: date | None,
        jmlomzetawal: Decimal | None,
        kdflow: str | None,
        updated_by: str | None,
    ) -> TransPendataan | None:
        trans_pendataan = TransPendataan(
            idpendataan=idpendataan,
            spt=spt,
            idwpdata=idwpdata,
            uruttgl=uruttgl,
            tarifpjk=tarifpjk,
            idupt=idupt,
            status=status,
            tglpendataan=tglpendataan,
            masaawal=masaawal,
            masaakhir=masaakhir,
            jmlomzetawal=jmlomzetawal,
            kdflow=kdflow,
            updated_by=updated_by,
        )
        return self.repository.update(idpendataan, trans_pendataan)

    def delete(self, idpendataan: int) -> bool:
        return self.repository.delete(idpendataan)
