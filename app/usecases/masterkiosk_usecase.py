from typing import List

from app.domain.entities.masterkiosk import MasterKiosk
from app.domain.repositories.masterkiosk_repository import MasterKioskRepository


class MasterKioskUseCase:

    def __init__(self, repository: MasterKioskRepository):
        self.repository = repository

    def get_all(self) -> List[MasterKiosk]:
        return self.repository.get_all()

    def get_by_id(self, idkios: int) -> MasterKiosk | None:
        return self.repository.get_by_id(idkios)

    def create(
        self,
        kodekiosk: str,
        datakiosk: str,
        level: str,
        status: str,
        idparent: int | None = None,
        created_by: str | None = None,
        updated_by: str | None = None,
    ) -> MasterKiosk:
        master_kiosk = MasterKiosk(
            idkios=None,
            kodekiosk=kodekiosk,
            datakiosk=datakiosk,
            level=level,
            status=status,
            idparent=idparent,
            created_by=created_by,
            updated_by=updated_by,
        )
        return self.repository.create(master_kiosk)

    def update(
        self,
        idkios: int,
        kodekiosk: str | None,
        datakiosk: str | None,
        level: str | None,
        status: str | None,
        idparent: int | None,
        updated_by: str | None,
    ) -> MasterKiosk | None:
        master_kiosk = MasterKiosk(
            idkios=idkios,
            kodekiosk=kodekiosk,
            datakiosk=datakiosk,
            level=level,
            status=status,
            idparent=idparent,
            updated_by=updated_by,
        )
        return self.repository.update(idkios, master_kiosk)

    def delete(self, idkios: int) -> bool:
        return self.repository.delete(idkios)
