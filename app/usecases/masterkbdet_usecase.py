from typing import List

from app.domain.entities.masterkbdet import MasterKbDet
from app.domain.repositories.masterkbdet_repository import MasterKbDetRepository


class MasterKbDetUseCase:

    def __init__(self, repository: MasterKbDetRepository):
        self.repository = repository

    def get_all(self) -> List[MasterKbDet]:
        return self.repository.get_all()

    def get_by_id(self, idkbdet: int) -> MasterKbDet | None:
        return self.repository.get_by_id(idkbdet)

    def create(
        self,
        idkb: int,
        idjnsd: int,
        created_by: str | None = None,
        updated_by: str | None = None,
    ) -> MasterKbDet:
        master_kbdet = MasterKbDet(
            idkbdet=None,
            idkb=idkb,
            idjnsd=idjnsd,
            created_by=created_by,
            updated_by=updated_by,
        )
        return self.repository.create(master_kbdet)

    def update(
        self,
        idkbdet: int,
        idkb: int | None,
        idjnsd: int | None,
        updated_by: str | None,
    ) -> MasterKbDet | None:
        master_kbdet = MasterKbDet(
            idkbdet=idkbdet,
            idkb=idkb,
            idjnsd=idjnsd,
            updated_by=updated_by,
        )
        return self.repository.update(idkbdet, master_kbdet)

    def delete(self, idkbdet: int) -> bool:
        return self.repository.delete(idkbdet)
