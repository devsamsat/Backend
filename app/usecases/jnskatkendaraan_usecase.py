from typing import List
from app.domain.entities.jnskatkendaraan import JnsKatKendaraan
from app.domain.repositories.jnskatkendaraan_repository import JnsKatKendaraanRepository


class JnsKatKendaraanUseCase:

    def __init__(self, repository: JnsKatKendaraanRepository):
        self.repository = repository

    def get_all(self) -> List[JnsKatKendaraan]:
        return self.repository.get_all()

    def get_by_id(self, katid: str) -> JnsKatKendaraan | None:
        return self.repository.get_by_id(katid)

    def create(self, jnskatkendaraan: JnsKatKendaraan) -> JnsKatKendaraan:
        return self.repository.create(jnskatkendaraan)

    def update(self, katid: str, jnskatkendaraan: JnsKatKendaraan) -> JnsKatKendaraan | None:
        return self.repository.update(katid, jnskatkendaraan)

    def delete(self, katid: str) -> bool:
        return self.repository.delete(katid)
