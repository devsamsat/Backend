from typing import List
from app.domain.entities.masterteks import MasterTeks
from app.domain.repositories.masterteks_repository import MasterTeksRepository


class MasterTeksUseCase:

    def __init__(self, repository: MasterTeksRepository):
        self.repository = repository

    def get_all(self) -> List[MasterTeks]:
        return self.repository.get_all()

    def get_by_id(self, idteks: int) -> MasterTeks | None:
        return self.repository.get_by_id(idteks)

    def create(
        self,
        datateks: str,
        status: str,
        created_by: str | None,
        updated_by: str | None,
    ) -> MasterTeks:
        teks = MasterTeks(
            idteks=None,
            datateks=datateks,
            status=status,
            created_by=created_by,
            updated_by=updated_by,
        )
        return self.repository.create(teks)

    def update(
        self,
        idteks: int,
        datateks: str | None,
        status: str | None,
        updated_by: str | None,
    ) -> MasterTeks | None:
        teks = MasterTeks(
            idteks=idteks,
            datateks=datateks,
            status=status,
            updated_by=updated_by,
        )
        return self.repository.update(idteks, teks)

    def delete(self, idteks: int) -> bool:
        return self.repository.delete(idteks)
