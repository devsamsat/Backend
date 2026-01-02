from typing import List

from app.domain.entities.masterreknrc import MasterRekNrc
from app.domain.repositories.masterreknrc_repository import MasterRekNrcRepository


class MasterRekNrcUseCase:

    def __init__(self, repository: MasterRekNrcRepository):
        self.repository = repository

    def get_all(self) -> List[MasterRekNrc]:
        return self.repository.get_all()

    def get_by_id(self, idreknrc: int) -> MasterRekNrc | None:
        return self.repository.get_by_id(idreknrc)

    def create(
        self,
        kdrek: str,
        mtglevel: str | None = None,
        nmrek: str | None = None,
        rek_type: str | None = None,
        created_by: str | None = None,
        updated_by: str | None = None,
    ) -> MasterRekNrc:
        master_reknrc = MasterRekNrc(
            idreknrc=None,
            kdrek=kdrek,
            mtglevel=mtglevel,
            nmrek=nmrek,
            rek_type=rek_type,
            created_by=created_by,
            updated_by=updated_by,
        )
        return self.repository.create(master_reknrc)

    def update(
        self,
        idreknrc: int,
        kdrek: str | None,
        mtglevel: str | None,
        nmrek: str | None,
        rek_type: str | None,
        updated_by: str | None,
    ) -> MasterRekNrc | None:
        master_reknrc = MasterRekNrc(
            idreknrc=idreknrc,
            kdrek=kdrek,
            mtglevel=mtglevel,
            nmrek=nmrek,
            rek_type=rek_type,
            updated_by=updated_by,
        )
        return self.repository.update(idreknrc, master_reknrc)

    def delete(self, idreknrc: int) -> bool:
        return self.repository.delete(idreknrc)
