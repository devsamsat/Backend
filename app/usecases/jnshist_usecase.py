from typing import List

from app.domain.entities.jnshist import JnsHist
from app.domain.repositories.jnshist_repository import JnsHistRepository


class JnsHistUseCase:

    def __init__(self, repository: JnsHistRepository):
        self.repository = repository

    def get_all(self) -> List[JnsHist]:
        return self.repository.get_all()

    def get_by_id(self, kdhist: str) -> JnsHist | None:
        return self.repository.get_by_id(kdhist)

    def create(
        self,
        kdhist: str,
        nmhist: str,
        kdflow: str | None,
        status: str | None,
        created_by: str | None,
        updated_by: str | None,
    ) -> JnsHist:
        jns_hist = JnsHist(
            kdhist=kdhist,
            nmhist=nmhist,
            kdflow=kdflow,
            status=status,
            created_by=created_by,
            updated_by=updated_by,
        )
        return self.repository.create(jns_hist)

    def update(
        self,
        kdhist: str,
        nmhist: str | None,
        kdflow: str | None,
        status: str | None,
        updated_by: str | None,
    ) -> JnsHist | None:
        jns_hist = JnsHist(
            kdhist=kdhist,
            nmhist=nmhist,
            kdflow=kdflow,
            status=status,
            updated_by=updated_by,
        )
        return self.repository.update(kdhist, jns_hist)

    def delete(self, kdhist: str) -> bool:
        return self.repository.delete(kdhist)
