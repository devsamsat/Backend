from typing import List
from app.domain.entities.jnsguna import JnsGuna
from app.domain.repositories.jnsguna_repository import JnsGunaRepository


class JnsGunaUseCase:

    def __init__(self, repository: JnsGunaRepository):
        self.repository = repository

    def get_all(self) -> List[JnsGuna]:
        return self.repository.get_all()

    def get_by_id(self, kdguna: str) -> JnsGuna | None:
        return self.repository.get_by_id(kdguna)

    def create(self, jnsguna: JnsGuna) -> JnsGuna:
        return self.repository.create(jnsguna)

    def update(self, kdguna: str, jnsguna: JnsGuna) -> JnsGuna | None:
        return self.repository.update(kdguna, jnsguna)

    def delete(self, kdguna: str) -> bool:
        return self.repository.delete(kdguna)
