from decimal import Decimal
from typing import List

from app.domain.entities.transstsdet import TransStsDet
from app.domain.repositories.transstsdet_repository import TransStsDetRepository


class TransStsDetUseCase:

    def __init__(self, repository: TransStsDetRepository):
        self.repository = repository

    def get_all(self) -> List[TransStsDet]:
        return self.repository.get_all()

    def get_by_id(self, idstsdet: int) -> TransStsDet | None:
        return self.repository.get_by_id(idstsdet)

    def create(
        self,
        idsts: int,
        idrekd: int,
        nilaists: Decimal,
        jenis: str,
        created_by: str | None = None,
        updated_by: str | None = None,
    ) -> TransStsDet:
        trans_sts_det = TransStsDet(
            idstsdet=None,
            idsts=idsts,
            idrekd=idrekd,
            nilaists=nilaists,
            jenis=jenis,
            created_by=created_by,
            updated_by=updated_by,
        )
        return self.repository.create(trans_sts_det)

    def update(
        self,
        idstsdet: int,
        idsts: int | None,
        idrekd: int | None,
        nilaists: Decimal | None,
        jenis: str | None,
        updated_by: str | None,
    ) -> TransStsDet | None:
        trans_sts_det = TransStsDet(
            idstsdet=idstsdet,
            idsts=idsts,
            idrekd=idrekd,
            nilaists=nilaists,
            jenis=jenis,
            updated_by=updated_by,
        )
        return self.repository.update(idstsdet, trans_sts_det)

    def delete(self, idstsdet: int) -> bool:
        return self.repository.delete(idstsdet)
