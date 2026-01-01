from datetime import date
from typing import List
from app.domain.entities.transhistpendataan import TransHistPendataan
from app.domain.repositories.transhistpendataan_repository import (
    TransHistPendataanRepository,
)


class TransHistPendataanUseCase:

    def __init__(self, repository: TransHistPendataanRepository):
        self.repository = repository

    def get_all(self) -> List[TransHistPendataan]:
        return self.repository.get_all()

    def get_by_id(self, idhistpendataan: int) -> TransHistPendataan | None:
        return self.repository.get_by_id(idhistpendataan)

    def create(
        self,
        idpendataan: int,
        spt: str,
        idwpdata: int,
        uruttgl: int,
        tarifpjk: float,
        idupt: int,
        histid: str,
        status: str,
        tglpendataan: date | None,
        masaawal: date | None,
        masaakhir: date | None,
        jmlomzetawal: float | None,
        kdflow: str | None,
        created_by: str | None,
        updated_by: str | None,
    ) -> TransHistPendataan:
        pendataan = TransHistPendataan(
            idhistpendataan=None,
            idpendataan=idpendataan,
            spt=spt,
            idwpdata=idwpdata,
            uruttgl=uruttgl,
            tarifpjk=tarifpjk,
            idupt=idupt,
            histid=histid,
            status=status,
            tglpendataan=tglpendataan,
            masaawal=masaawal,
            masaakhir=masaakhir,
            jmlomzetawal=jmlomzetawal,
            kdflow=kdflow,
            created_by=created_by,
            updated_by=updated_by,
        )
        return self.repository.create(pendataan)

    def update(
        self,
        idhistpendataan: int,
        idpendataan: int | None,
        spt: str | None,
        idwpdata: int | None,
        uruttgl: int | None,
        tarifpjk: float | None,
        idupt: int | None,
        histid: str | None,
        status: str | None,
        tglpendataan: date | None,
        masaawal: date | None,
        masaakhir: date | None,
        jmlomzetawal: float | None,
        kdflow: str | None,
        updated_by: str | None,
    ) -> TransHistPendataan | None:
        pendataan = TransHistPendataan(
            idhistpendataan=idhistpendataan,
            idpendataan=idpendataan,
            spt=spt,
            idwpdata=idwpdata,
            uruttgl=uruttgl,
            tarifpjk=tarifpjk,
            idupt=idupt,
            histid=histid,
            status=status,
            tglpendataan=tglpendataan,
            masaawal=masaawal,
            masaakhir=masaakhir,
            jmlomzetawal=jmlomzetawal,
            kdflow=kdflow,
            updated_by=updated_by,
        )
        return self.repository.update(idhistpendataan, pendataan)

    def delete(self, idhistpendataan: int) -> bool:
        return self.repository.delete(idhistpendataan)
