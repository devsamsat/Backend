from typing import List

from app.domain.entities.jnsmilik import JnsMilik
from app.domain.repositories.jnsmilik_repository import JnsMilikRepository


class JnsMilikUseCase:

    def __init__(self, repository: JnsMilikRepository):
        self.repository = repository

    def get_all(self) -> List[JnsMilik]:
        return self.repository.get_all()

    def get_by_id(self, kdmilik: str) -> JnsMilik | None:
        return self.repository.get_by_id(kdmilik)

    def create(
        self,
        kdmilik: str,
        milik: str,
        bpkpid: str,
        status: str | None,
        created_by: str | None,
        updated_by: str | None,
    ) -> JnsMilik:
        jns_milik = JnsMilik(
            kdmilik=kdmilik,
            milik=milik,
            bpkpid=bpkpid,
            status=status,
            created_by=created_by,
            updated_by=updated_by,
        )
        return self.repository.create(jns_milik)

    def update(
        self,
        kdmilik: str,
        milik: str | None,
        bpkpid: str | None,
        status: str | None,
        updated_by: str | None,
    ) -> JnsMilik | None:
        jns_milik = JnsMilik(
            kdmilik=kdmilik,
            milik=milik,
            bpkpid=bpkpid,
            status=status,
            updated_by=updated_by,
        )
        return self.repository.update(kdmilik, jns_milik)

    def delete(self, kdmilik: str) -> bool:
        return self.repository.delete(kdmilik)
