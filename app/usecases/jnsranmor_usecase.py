from typing import List

from app.domain.entities.jnsranmor import JnsRanmor
from app.domain.repositories.jnsranmor_repository import JnsRanmorRepository


class JnsRanmorUseCase:

    def __init__(self, repository: JnsRanmorRepository):
        self.repository = repository

    def get_all(self) -> List[JnsRanmor]:
        return self.repository.get_all()

    def get_by_id(self, kdranmor: str) -> JnsRanmor | None:
        return self.repository.get_by_id(kdranmor)

    def create(
        self,
        kdranmor: str,
        nmranmor: str,
        snid: str,
        status: str | None,
        created_by: str | None,
        updated_by: str | None,
    ) -> JnsRanmor:
        jns_ranmor = JnsRanmor(
            kdranmor=kdranmor,
            nmranmor=nmranmor,
            snid=snid,
            status=status,
            created_by=created_by,
            updated_by=updated_by,
        )
        return self.repository.create(jns_ranmor)

    def update(
        self,
        kdranmor: str,
        nmranmor: str | None,
        snid: str | None,
        status: str | None,
        updated_by: str | None,
    ) -> JnsRanmor | None:
        jns_ranmor = JnsRanmor(
            kdranmor=kdranmor,
            nmranmor=nmranmor,
            snid=snid,
            status=status,
            updated_by=updated_by,
        )
        return self.repository.update(kdranmor, jns_ranmor)

    def delete(self, kdranmor: str) -> bool:
        return self.repository.delete(kdranmor)
