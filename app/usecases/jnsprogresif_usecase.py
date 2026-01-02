from typing import List

from app.domain.entities.jnsprogresif import JnsProgresif
from app.domain.repositories.jnsprogresif_repository import JnsProgresifRepository


class JnsProgresifUseCase:

    def __init__(self, repository: JnsProgresifRepository):
        self.repository = repository

    def get_all(self) -> List[JnsProgresif]:
        return self.repository.get_all()

    def get_by_id(self, kdprogresif: int) -> JnsProgresif | None:
        return self.repository.get_by_id(kdprogresif)

    def create(
        self,
        kdprogresif: int,
        progresifr2: float,
        progresifr4: float,
        created_by: str | None,
        updated_by: str | None,
    ) -> JnsProgresif:
        jns_progresif = JnsProgresif(
            kdprogresif=kdprogresif,
            progresifr2=progresifr2,
            progresifr4=progresifr4,
            created_by=created_by,
            updated_by=updated_by,
        )
        return self.repository.create(jns_progresif)

    def update(
        self,
        kdprogresif: int,
        progresifr2: float | None,
        progresifr4: float | None,
        updated_by: str | None,
    ) -> JnsProgresif | None:
        jns_progresif = JnsProgresif(
            kdprogresif=kdprogresif,
            progresifr2=progresifr2,
            progresifr4=progresifr4,
            updated_by=updated_by,
        )
        return self.repository.update(kdprogresif, jns_progresif)

    def delete(self, kdprogresif: int) -> bool:
        return self.repository.delete(kdprogresif)
