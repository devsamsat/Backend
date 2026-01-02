from typing import List

from app.domain.entities.masterkaupt import MasterKaupt
from app.domain.repositories.masterkaupt_repository import MasterKauptRepository


class MasterKauptUseCase:

    def __init__(self, repository: MasterKauptRepository):
        self.repository = repository

    def get_all(self) -> List[MasterKaupt]:
        return self.repository.get_all()

    def get_by_id(self, idkaupt: int) -> MasterKaupt | None:
        return self.repository.get_by_id(idkaupt)

    def create(
        self,
        idupt: int,
        idpegawai: int | None = None,
        created_by: str | None = None,
        updated_by: str | None = None,
    ) -> MasterKaupt:
        master_kaupt = MasterKaupt(
            idkaupt=None,
            idupt=idupt,
            idpegawai=idpegawai,
            created_by=created_by,
            updated_by=updated_by,
        )
        return self.repository.create(master_kaupt)

    def update(
        self,
        idkaupt: int,
        idupt: int | None,
        idpegawai: int | None,
        updated_by: str | None,
    ) -> MasterKaupt | None:
        master_kaupt = MasterKaupt(
            idkaupt=idkaupt,
            idupt=idupt,
            idpegawai=idpegawai,
            updated_by=updated_by,
        )
        return self.repository.update(idkaupt, master_kaupt)

    def delete(self, idkaupt: int) -> bool:
        return self.repository.delete(idkaupt)
