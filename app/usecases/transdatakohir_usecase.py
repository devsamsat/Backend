from datetime import date
from typing import List

from app.domain.entities.transdatakohir import TransDataKohir
from app.domain.repositories.transdatakohir_repository import TransDataKohirRepository


class TransDataKohirUseCase:

    def __init__(self, repository: TransDataKohirRepository):
        self.repository = repository

    def get_all(self) -> List[TransDataKohir]:
        return self.repository.get_all()

    def get_by_id(self, idkohir: int) -> TransDataKohir | None:
        return self.repository.get_by_id(idkohir)

    def create(
        self,
        penagih: str,
        idwp: int,
        masaawal: date | None = None,
        masaakhir: date | None = None,
        tglpenetapan: date | None = None,
        tglkurangbayar: date | None = None,
        keterangan: str | None = None,
        idupt: int | None = None,
        skrupt: str | None = None,
        validjr: str | None = None,
        validjrby: str | None = None,
        validpol: str | None = None,
        validpolby: str | None = None,
        ntpd: str | None = None,
        tglntpd: date | None = None,
        idbank: str | None = None,
        created_by: str | None = None,
        updated_by: str | None = None,
    ) -> TransDataKohir:
        trans_data_kohir = TransDataKohir(
            idkohir=None,
            penagih=penagih,
            idwp=idwp,
            masaawal=masaawal,
            masaakhir=masaakhir,
            tglpenetapan=tglpenetapan,
            tglkurangbayar=tglkurangbayar,
            keterangan=keterangan,
            idupt=idupt,
            skrupt=skrupt,
            validjr=validjr,
            validjrby=validjrby,
            validpol=validpol,
            validpolby=validpolby,
            ntpd=ntpd,
            tglntpd=tglntpd,
            idbank=idbank,
            created_by=created_by,
            updated_by=updated_by,
        )
        return self.repository.create(trans_data_kohir)

    def update(
        self,
        idkohir: int,
        penagih: str | None,
        idwp: int | None,
        masaawal: date | None,
        masaakhir: date | None,
        tglpenetapan: date | None,
        tglkurangbayar: date | None,
        keterangan: str | None,
        idupt: int | None,
        skrupt: str | None,
        validjr: str | None,
        validjrby: str | None,
        validpol: str | None,
        validpolby: str | None,
        ntpd: str | None,
        tglntpd: date | None,
        idbank: str | None,
        updated_by: str | None,
    ) -> TransDataKohir | None:
        trans_data_kohir = TransDataKohir(
            idkohir=idkohir,
            penagih=penagih,
            idwp=idwp,
            masaawal=masaawal,
            masaakhir=masaakhir,
            tglpenetapan=tglpenetapan,
            tglkurangbayar=tglkurangbayar,
            keterangan=keterangan,
            idupt=idupt,
            skrupt=skrupt,
            validjr=validjr,
            validjrby=validjrby,
            validpol=validpol,
            validpolby=validpolby,
            ntpd=ntpd,
            tglntpd=tglntpd,
            idbank=idbank,
            updated_by=updated_by,
        )
        return self.repository.update(idkohir, trans_data_kohir)

    def delete(self, idkohir: int) -> bool:
        return self.repository.delete(idkohir)
