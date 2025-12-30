from typing import List

from app.domain.entities.masterabdet import MasterAbDet
from app.domain.repositories.masterabdet_repository import MasterAbDetRepository


class MasterAbDetUseCase:

    def __init__(self, repository: MasterAbDetRepository):
        self.repository = repository

    def get_all(self) -> List[MasterAbDet]:
        return self.repository.get_all()

    def get_by_id(self, idabdet: int) -> MasterAbDet | None:
        return self.repository.get_by_id(idabdet)

    def create(
        self,
        idab: int,
        idjnsd: int,
        created_by: str | None = None,
        updated_by: str | None = None,
    ) -> MasterAbDet:
        master_ab_det = MasterAbDet(
            idabdet=None,
            idab=idab,
            idjnsd=idjnsd,
            created_by=created_by,
            updated_by=updated_by,
        )
        return self.repository.create(master_ab_det)

    def update(
        self,
        idabdet: int,
        idab: int | None,
        idjnsd: int | None,
        updated_by: str | None,
    ) -> MasterAbDet | None:
        master_ab_det = MasterAbDet(
            idabdet=idabdet,
            idab=idab,
            idjnsd=idjnsd,
            updated_by=updated_by,
        )
        return self.repository.update(idabdet, master_ab_det)

    def delete(self, idabdet: int) -> bool:
        return self.repository.delete(idabdet)
