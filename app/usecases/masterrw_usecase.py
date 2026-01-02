from typing import List

from app.domain.entities.masterrw import MasterRw
from app.domain.repositories.masterrw_repository import MasterRwRepository


class MasterRwUseCase:

    def __init__(self, repository: MasterRwRepository):
        self.repository = repository

    def get_all(self) -> List[MasterRw]:
        return self.repository.get_all()

    def get_by_id(self, idrw: int) -> MasterRw | None:
        return self.repository.get_by_id(idrw)

    def create(
        self,
        idkelurahan: int,
        alamat: str,
        status: str,
        kdrw: str | None = None,
        created_by: str | None = None,
        updated_by: str | None = None,
    ) -> MasterRw:
        master_rw = MasterRw(
            idrw=None,
            idkelurahan=idkelurahan,
            alamat=alamat,
            status=status,
            kdrw=kdrw,
            created_by=created_by,
            updated_by=updated_by,
        )
        return self.repository.create(master_rw)

    def update(
        self,
        idrw: int,
        idkelurahan: int | None,
        alamat: str | None,
        status: str | None,
        kdrw: str | None,
        updated_by: str | None,
    ) -> MasterRw | None:
        master_rw = MasterRw(
            idrw=idrw,
            idkelurahan=idkelurahan,
            alamat=alamat,
            status=status,
            kdrw=kdrw,
            updated_by=updated_by,
        )
        return self.repository.update(idrw, master_rw)

    def delete(self, idrw: int) -> bool:
        return self.repository.delete(idrw)
