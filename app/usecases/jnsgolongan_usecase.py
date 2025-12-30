from typing import List
from app.domain.entities.jnsgolongan import JnsGolongan
from app.domain.repositories.jnsgolongan_repository import JnsGolonganRepository


class JnsGolonganUseCase:

    def __init__(self, repository: JnsGolonganRepository):
        self.repository = repository

    def get_all(self) -> List[JnsGolongan]:
        return self.repository.get_all()

    def get_by_id(self, jnsgolid: str) -> JnsGolongan | None:
        return self.repository.get_by_id(jnsgolid)

    def create(self, jnsgolongan: JnsGolongan) -> JnsGolongan:
        return self.repository.create(jnsgolongan)

    def update(self, jnsgolid: str, jnsgolongan: JnsGolongan) -> JnsGolongan | None:
        return self.repository.update(jnsgolid, jnsgolongan)

    def delete(self, jnsgolid: str) -> bool:
        return self.repository.delete(jnsgolid)
