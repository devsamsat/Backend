from typing import List
from app.domain.entities.transhistpendataandet import TransHistPendataanDet
from app.domain.repositories.transhistpendataandet_repository import (
    TransHistPendataanDetRepository,
)


class TransHistPendataanDetUseCase:

    def __init__(self, repository: TransHistPendataanDetRepository):
        self.repository = repository

    def get_all(self) -> List[TransHistPendataanDet]:
        return self.repository.get_all()

    def get_by_id(self, idhistpendataandet: int) -> TransHistPendataanDet | None:
        return self.repository.get_by_id(idhistpendataandet)

    def create(
        self,
        idhistpendataan: int,
        idpenetapan: int,
        nourut: int,
        transid: str,
        ket1: str,
        usahaid: int,
        tarifpajak: float,
        histid: str,
        status: str,
        lokasi: str | None,
        created_by: str | None,
        updated_by: str | None,
    ) -> TransHistPendataanDet:
        pendataan_det = TransHistPendataanDet(
            idhistpendataandet=None,
            idhistpendataan=idhistpendataan,
            idpenetapan=idpenetapan,
            nourut=nourut,
            transid=transid,
            ket1=ket1,
            usahaid=usahaid,
            tarifpajak=tarifpajak,
            histid=histid,
            status=status,
            lokasi=lokasi,
            created_by=created_by,
            updated_by=updated_by,
        )
        return self.repository.create(pendataan_det)

    def update(
        self,
        idhistpendataandet: int,
        idhistpendataan: int | None,
        idpenetapan: int | None,
        nourut: int | None,
        transid: str | None,
        ket1: str | None,
        usahaid: int | None,
        tarifpajak: float | None,
        histid: str | None,
        status: str | None,
        lokasi: str | None,
        updated_by: str | None,
    ) -> TransHistPendataanDet | None:
        pendataan_det = TransHistPendataanDet(
            idhistpendataandet=idhistpendataandet,
            idhistpendataan=idhistpendataan,
            idpenetapan=idpenetapan,
            nourut=nourut,
            transid=transid,
            ket1=ket1,
            usahaid=usahaid,
            tarifpajak=tarifpajak,
            histid=histid,
            status=status,
            lokasi=lokasi,
            updated_by=updated_by,
        )
        return self.repository.update(idhistpendataandet, pendataan_det)

    def delete(self, idhistpendataandet: int) -> bool:
        return self.repository.delete(idhistpendataandet)
