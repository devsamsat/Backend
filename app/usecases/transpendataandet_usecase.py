from decimal import Decimal
from typing import List

from app.domain.entities.transpendataandet import TransPendataanDet
from app.domain.repositories.transpendataandet_repository import (
    TransPendataanDetRepository,
)


class TransPendataanDetUseCase:

    def __init__(self, repository: TransPendataanDetRepository):
        self.repository = repository

    def get_all(self) -> List[TransPendataanDet]:
        return self.repository.get_all()

    def get_by_id(self, idpendataandet: int) -> TransPendataanDet | None:
        return self.repository.get_by_id(idpendataandet)

    def create(
        self,
        idpendataan: int,
        idpenetapan: int,
        nourut: int,
        transid: str,
        ket1: str,
        usahaid: int,
        tarifpajak: Decimal,
        status: str,
        lokasi: str | None = None,
        created_by: str | None = None,
        updated_by: str | None = None,
    ) -> TransPendataanDet:
        trans_pendataan_det = TransPendataanDet(
            idpendataandet=None,
            idpendataan=idpendataan,
            idpenetapan=idpenetapan,
            nourut=nourut,
            transid=transid,
            ket1=ket1,
            usahaid=usahaid,
            tarifpajak=tarifpajak,
            status=status,
            lokasi=lokasi,
            created_by=created_by,
            updated_by=updated_by,
        )
        return self.repository.create(trans_pendataan_det)

    def update(
        self,
        idpendataandet: int,
        idpendataan: int | None,
        idpenetapan: int | None,
        nourut: int | None,
        transid: str | None,
        ket1: str | None,
        usahaid: int | None,
        tarifpajak: Decimal | None,
        status: str | None,
        lokasi: str | None,
        updated_by: str | None,
    ) -> TransPendataanDet | None:
        trans_pendataan_det = TransPendataanDet(
            idpendataandet=idpendataandet,
            idpendataan=idpendataan,
            idpenetapan=idpenetapan,
            nourut=nourut,
            transid=transid,
            ket1=ket1,
            usahaid=usahaid,
            tarifpajak=tarifpajak,
            status=status,
            lokasi=lokasi,
            updated_by=updated_by,
        )
        return self.repository.update(idpendataandet, trans_pendataan_det)

    def delete(self, idpendataandet: int) -> bool:
        return self.repository.delete(idpendataandet)
