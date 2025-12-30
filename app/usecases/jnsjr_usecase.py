from typing import List
from app.domain.entities.jnsjr import JnsJr
from app.domain.repositories.jnsjr_repository import JnsJrRepository


class JnsJrUseCase:

    def __init__(self, repository: JnsJrRepository):
        self.repository = repository

    def get_all(self) -> List[JnsJr]:
        return self.repository.get_all()

    def get_by_id(self, jnsjrid: str) -> JnsJr | None:
        return self.repository.get_by_id(jnsjrid)

    def create(self, jnsjr: JnsJr) -> JnsJr:
        return self.repository.create(jnsjr)

    def update(self, jnsjrid: str, jnsjr: JnsJr) -> JnsJr | None:
        return self.repository.update(jnsjrid, jnsjr)

    def delete(self, jnsjrid: str) -> bool:
        return self.repository.delete(jnsjrid)
