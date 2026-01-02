from typing import List

from app.domain.entities.masterrekd import MasterRekd
from app.domain.repositories.masterrekd_repository import MasterRekdRepository


class MasterRekdUseCase:

    def __init__(self, repository: MasterRekdRepository):
        self.repository = repository

    def get_all(self) -> List[MasterRekd]:
        return self.repository.get_all()

    def get_by_id(self, idrekd: int) -> MasterRekd | None:
        return self.repository.get_by_id(idrekd)

    def create(
        self,
        kdrek: str,
        idparent: int | None = None,
        mtglevel: str | None = None,
        nmrek: str | None = None,
        kdjnspjk: str | None = None,
        rek_type: str | None = None,
        status: str | None = None,
        created_by: str | None = None,
        updated_by: str | None = None,
    ) -> MasterRekd:
        master_rekd = MasterRekd(
            idrekd=None,
            kdrek=kdrek,
            idparent=idparent,
            mtglevel=mtglevel,
            nmrek=nmrek,
            kdjnspjk=kdjnspjk,
            rek_type=rek_type,
            status=status,
            created_by=created_by,
            updated_by=updated_by,
        )
        return self.repository.create(master_rekd)

    def update(
        self,
        idrekd: int,
        kdrek: str | None,
        idparent: int | None,
        mtglevel: str | None,
        nmrek: str | None,
        kdjnspjk: str | None,
        rek_type: str | None,
        status: str | None,
        updated_by: str | None,
    ) -> MasterRekd | None:
        master_rekd = MasterRekd(
            idrekd=idrekd,
            kdrek=kdrek,
            idparent=idparent,
            mtglevel=mtglevel,
            nmrek=nmrek,
            kdjnspjk=kdjnspjk,
            rek_type=rek_type,
            status=status,
            updated_by=updated_by,
        )
        return self.repository.update(idrekd, master_rekd)

    def delete(self, idrekd: int) -> bool:
        return self.repository.delete(idrekd)
