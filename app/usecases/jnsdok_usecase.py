from typing import List
from app.domain.entities.jnsdok import JnsDok
from app.domain.repositories.jnsdok_repository import JnsDokRepository


class JnsDokUseCase:

    def __init__(self, repository: JnsDokRepository):
        self.repository = repository

    def get_all(self) -> List[JnsDok]:
        return self.repository.get_all()

    def get_by_id(self, kddok: str) -> JnsDok | None:
        return self.repository.get_by_id(kddok)

    def create(self, jnsdok: JnsDok) -> JnsDok:
        return self.repository.create(jnsdok)

    def update(self, kddok: str, jnsdok: JnsDok) -> JnsDok | None:
        return self.repository.update(kddok, jnsdok)

    def delete(self, kddok: str) -> bool:
        return self.repository.delete(kddok)
