from datetime import date
from decimal import Decimal
from typing import List

from app.domain.entities.transpenetapan import TransPenetapan
from app.domain.repositories.transpenetapan_repository import TransPenetapanRepository


class TransPenetapanUseCase:

    def __init__(self, repository: TransPenetapanRepository):
        self.repository = repository

    def get_all(self) -> List[TransPenetapan]:
        return self.repository.get_all()

    def get_by_id(self, idpenetapan: int) -> TransPenetapan | None:
        return self.repository.get_by_id(idpenetapan)

    def create(
        self,
        idkohir: int,
        idwpdata: int,
        uruttgl: int,
        tarifpajak: Decimal,
        statbayar: str,
        status: str,
        nokohir: str | None = None,
        tglpenetapan: date | None = None,
        tgljatuhtempo: date | None = None,
        masaawal: date | None = None,
        masaakhir: date | None = None,
        jmlomzetawal: Decimal | None = None,
        denda: Decimal | None = None,
        kenaikan: Decimal | None = None,
        tglbayar: date | None = None,
        jmlbayar: Decimal | None = None,
        tglkurangbayar: date | None = None,
        jmlkurangbayar: Decimal | None = None,
        jmlperingatan: int | None = None,
        kdflow: str | None = None,
        opsid: str | None = None,
        opsprov: Decimal | None = None,
        opskota: Decimal | None = None,
        dendaopsprov: Decimal | None = None,
        dendaopskota: Decimal | None = None,
        created_by: str | None = None,
        updated_by: str | None = None,
    ) -> TransPenetapan:
        trans_penetapan = TransPenetapan(
            idpenetapan=None,
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
        return self.repository.create(trans_penetapan)

    def update(
        self,
        idpenetapan: int,
        idkohir: int | None,
        idwpdata: int | None,
        uruttgl: int | None,
        tarifpajak: Decimal | None,
        statbayar: str | None,
        status: str | None,
        nokohir: str | None,
        tglpenetapan: date | None,
        tgljatuhtempo: date | None,
        masaawal: date | None,
        masaakhir: date | None,
        jmlomzetawal: Decimal | None,
        denda: Decimal | None,
        kenaikan: Decimal | None,
        tglbayar: date | None,
        jmlbayar: Decimal | None,
        tglkurangbayar: date | None,
        jmlkurangbayar: Decimal | None,
        jmlperingatan: int | None,
        kdflow: str | None,
        opsid: str | None,
        opsprov: Decimal | None,
        opskota: Decimal | None,
        dendaopsprov: Decimal | None,
        dendaopskota: Decimal | None,
        updated_by: str | None,
    ) -> TransPenetapan | None:
        trans_penetapan = TransPenetapan(
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
        return self.repository.update(idpenetapan, trans_penetapan)

    def delete(self, idpenetapan: int) -> bool:
        return self.repository.delete(idpenetapan)
