from typing import List

from app.domain.entities.masterrt import MasterRt
from app.domain.repositories.masterrt_repository import MasterRtRepository


class MasterRtUseCase:

    def __init__(self, repository: MasterRtRepository):
        self.repository = repository

    def get_all(self) -> List[MasterRt]:
        return self.repository.get_all()

    def get_by_id(self, idrt: int) -> MasterRt | None:
        return self.repository.get_by_id(idrt)

    def create(
        self,
        idrw: int,
        status: str,
        kdrt: str | None = None,
        created_by: str | None = None,
        updated_by: str | None = None,
    ) -> MasterRt:
        master_rt = MasterRt(
            idrt=None,
            idrw=idrw,
            status=status,
            kdrt=kdrt,
            created_by=created_by,
            updated_by=updated_by,
        )
        return self.repository.create(master_rt)

    def update(
        self,
        idrt: int,
        idrw: int | None,
        status: str | None,
        kdrt: str | None,
        updated_by: str | None,
    ) -> MasterRt | None:
        master_rt = MasterRt(
            idrt=idrt,
            idrw=idrw,
            status=status,
            kdrt=kdrt,
            updated_by=updated_by,
        )
        return self.repository.update(idrt, master_rt)

    def delete(self, idrt: int) -> bool:
        return self.repository.delete(idrt)
