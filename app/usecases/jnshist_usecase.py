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

    def create(self, jnshist: JnsHist) -> JnsHist:
        return self.repository.create(jnshist)

    def update(self, kdhist: str, jnshist: JnsHist) -> JnsHist | None:
        return self.repository.update(kdhist, jnshist)

    def delete(self, kdhist: str) -> bool:
        return self.repository.delete(kdhist)
