from typing import List

from app.domain.entities.jnstarif import JnsTarif
from app.domain.repositories.jnstarif_repository import JnsTarifRepository


class JnsTarifUseCase:

    def __init__(self, repository: JnsTarifRepository):
        self.repository = repository

    def get_all(self) -> List[JnsTarif]:
        return self.repository.get_all()

    def get_by_id(self, kdjnstarif: str) -> JnsTarif | None:
        return self.repository.get_by_id(kdjnstarif)

    def create(
        self,
        kdjnstarif: str,
        nmjnstarif: str,
        idupt: int,
        jnskendid: str | None,
        idrekd: int | None,
        status: str | None,
        created_by: str | None,
        updated_by: str | None,
    ) -> JnsTarif:
        jns_tarif = JnsTarif(
            kdjnstarif=kdjnstarif,
            nmjnstarif=nmjnstarif,
            idupt=idupt,
            jnskendid=jnskendid,
            idrekd=idrekd,
            status=status,
            created_by=created_by,
            updated_by=updated_by,
        )
        return self.repository.create(jns_tarif)

    def update(
        self,
        kdjnstarif: str,
        nmjnstarif: str | None,
        idupt: int | None,
        jnskendid: str | None,
        idrekd: int | None,
        status: str | None,
        updated_by: str | None,
    ) -> JnsTarif | None:
        jns_tarif = JnsTarif(
            kdjnstarif=kdjnstarif,
            nmjnstarif=nmjnstarif,
            idupt=idupt,
            jnskendid=jnskendid,
            idrekd=idrekd,
            status=status,
            updated_by=updated_by,
        )
        return self.repository.update(kdjnstarif, jns_tarif)

    def delete(self, kdjnstarif: str) -> bool:
        return self.repository.delete(kdjnstarif)
