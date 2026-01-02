from typing import List

from app.domain.entities.masterjnspendapatan import MasterJnsPendapatan
from app.domain.repositories.masterjnspendapatan_repository import (
    MasterJnsPendapatanRepository,
)


class MasterJnsPendapatanUseCase:

    def __init__(self, repository: MasterJnsPendapatanRepository):
        self.repository = repository

    def get_all(self) -> List[MasterJnsPendapatan]:
        return self.repository.get_all()

    def get_by_id(self, idjnsd: int) -> MasterJnsPendapatan | None:
        return self.repository.get_by_id(idjnsd)

    def create(
        self,
        nmjnspendapatan: str,
        parentid: int | None = None,
        kdrek: str | None = None,
        jatuhtempo: int | None = None,
        status: str | None = None,
        selfassessment: str | None = None,
        katid: str | None = None,
        created_by: str | None = None,
        updated_by: str | None = None,
    ) -> MasterJnsPendapatan:
        master_jns_pendapatan = MasterJnsPendapatan(
            idjnsd=None,
            nmjnspendapatan=nmjnspendapatan,
            parentid=parentid,
            kdrek=kdrek,
            jatuhtempo=jatuhtempo,
            status=status,
            selfassessment=selfassessment,
            katid=katid,
            created_by=created_by,
            updated_by=updated_by,
        )
        return self.repository.create(master_jns_pendapatan)

    def update(
        self,
        idjnsd: int,
        nmjnspendapatan: str | None,
        parentid: int | None,
        kdrek: str | None,
        jatuhtempo: int | None,
        status: str | None,
        selfassessment: str | None,
        katid: str | None,
        updated_by: str | None,
    ) -> MasterJnsPendapatan | None:
        master_jns_pendapatan = MasterJnsPendapatan(
            idjnsd=idjnsd,
            nmjnspendapatan=nmjnspendapatan,
            parentid=parentid,
            kdrek=kdrek,
            jatuhtempo=jatuhtempo,
            status=status,
            selfassessment=selfassessment,
            katid=katid,
            updated_by=updated_by,
        )
        return self.repository.update(idjnsd, master_jns_pendapatan)

    def delete(self, idjnsd: int) -> bool:
        return self.repository.delete(idjnsd)
