from datetime import date
from typing import List
from app.domain.entities.transhistpenetapan import TransHistPenetapan
from app.domain.repositories.transhistpenetapan_repository import (
    TransHistPenetapanRepository,
)


class TransHistPenetapanUseCase:

    def __init__(self, repository: TransHistPenetapanRepository):
        self.repository = repository

    def get_all(self) -> List[TransHistPenetapan]:
        return self.repository.get_all()

    def get_by_id(self, idhistpenetapan: int) -> TransHistPenetapan | None:
        return self.repository.get_by_id(idhistpenetapan)

    def create(
        self,
        idpenetapan: int,
        idkohir: int,
        idwpdata: int,
        uruttgl: int,
        tarifpajak: float,
        statbayar: str,
        status: str,
        nokohir: str | None,
        tglpenetapan: date | None,
        tgljatuhtempo: date | None,
        masaawal: date | None,
        masaakhir: date | None,
        jmlomzetawal: float | None,
        denda: float | None,
        kenaikan: float | None,
        tglbayar: date | None,
        jmlbayar: float | None,
        tglkurangbayar: date | None,
        jmlkurangbayar: float | None,
        jmlperingatan: int | None,
        kdflow: str | None,
        opsid: str | None,
        opsprov: float | None,
        opskota: float | None,
        dendaopsprov: float | None,
        dendaopskota: float | None,
        created_by: str | None,
        updated_by: str | None,
    ) -> TransHistPenetapan:
        penetapan = TransHistPenetapan(
            idhistpenetapan=None,
            idpenetapan=idpenetapan,
            idkohir=idkohir,
            idwpdata=idwpdata,
            uruttgl=uruttgl,
            tarifpajak=tarifpajak,
            statbayar=statbayar,
            status=status,
            nokohir=nokohir,
            tglpenetapan=tglpenetapan,
            tgljatuhtempo=tgljatuhtempo,
            masaawal=masaawal,
            masaakhir=masaakhir,
            jmlomzetawal=jmlomzetawal,
            denda=denda,
            kenaikan=kenaikan,
            tglbayar=tglbayar,
            jmlbayar=jmlbayar,
            tglkurangbayar=tglkurangbayar,
            jmlkurangbayar=jmlkurangbayar,
            jmlperingatan=jmlperingatan,
            kdflow=kdflow,
            opsid=opsid,
            opsprov=opsprov,
            opskota=opskota,
            dendaopsprov=dendaopsprov,
            dendaopskota=dendaopskota,
            created_by=created_by,
            updated_by=updated_by,
        )
        return self.repository.create(penetapan)

    def update(
        self,
        idhistpenetapan: int,
        idpenetapan: int | None,
        idkohir: int | None,
        idwpdata: int | None,
        uruttgl: int | None,
        tarifpajak: float | None,
        statbayar: str | None,
        status: str | None,
        nokohir: str | None,
        tglpenetapan: date | None,
        tgljatuhtempo: date | None,
        masaawal: date | None,
        masaakhir: date | None,
        jmlomzetawal: float | None,
        denda: float | None,
        kenaikan: float | None,
        tglbayar: date | None,
        jmlbayar: float | None,
        tglkurangbayar: date | None,
        jmlkurangbayar: float | None,
        jmlperingatan: int | None,
        kdflow: str | None,
        opsid: str | None,
        opsprov: float | None,
        opskota: float | None,
        dendaopsprov: float | None,
        dendaopskota: float | None,
        updated_by: str | None,
    ) -> TransHistPenetapan | None:
        penetapan = TransHistPenetapan(
            idhistpenetapan=idhistpenetapan,
            idpenetapan=idpenetapan,
            idkohir=idkohir,
            idwpdata=idwpdata,
            uruttgl=uruttgl,
            tarifpajak=tarifpajak,
            statbayar=statbayar,
            status=status,
            nokohir=nokohir,
            tglpenetapan=tglpenetapan,
            tgljatuhtempo=tgljatuhtempo,
            masaawal=masaawal,
            masaakhir=masaakhir,
            jmlomzetawal=jmlomzetawal,
            denda=denda,
            kenaikan=kenaikan,
            tglbayar=tglbayar,
            jmlbayar=jmlbayar,
            tglkurangbayar=tglkurangbayar,
            jmlkurangbayar=jmlkurangbayar,
            jmlperingatan=jmlperingatan,
            kdflow=kdflow,
            opsid=opsid,
            opsprov=opsprov,
            opskota=opskota,
            dendaopsprov=dendaopsprov,
            dendaopskota=dendaopskota,
            updated_by=updated_by,
        )
        return self.repository.update(idhistpenetapan, penetapan)

    def delete(self, idhistpenetapan: int) -> bool:
        return self.repository.delete(idhistpenetapan)
