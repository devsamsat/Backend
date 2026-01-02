from typing import List

from app.domain.entities.masterkelurahan import MasterKelurahan
from app.domain.repositories.masterkelurahan_repository import MasterKelurahanRepository


class MasterKelurahanUseCase:

    def __init__(self, repository: MasterKelurahanRepository):
        self.repository = repository

    def get_all(self) -> List[MasterKelurahan]:
        return self.repository.get_all()

    def get_by_id(self, idkelurahan: int) -> MasterKelurahan | None:
        return self.repository.get_by_id(idkelurahan)

    def create(
        self,
        idkecamatan: int,
        nmkelurahan: str,
        alamat: str,
        telepon: str,
        status: str,
        kdkelurahan: str | None = None,
        kodepos: str | None = None,
        created_by: str | None = None,
        updated_by: str | None = None,
    ) -> MasterKelurahan:
        master_kelurahan = MasterKelurahan(
            idkelurahan=None,
            idkecamatan=idkecamatan,
            nmkelurahan=nmkelurahan,
            alamat=alamat,
            telepon=telepon,
            status=status,
            kdkelurahan=kdkelurahan,
            kodepos=kodepos,
            created_by=created_by,
            updated_by=updated_by,
        )
        return self.repository.create(master_kelurahan)

    def update(
        self,
        idkelurahan: int,
        idkecamatan: int | None,
        nmkelurahan: str | None,
        alamat: str | None,
        telepon: str | None,
        status: str | None,
        kdkelurahan: str | None,
        kodepos: str | None,
        updated_by: str | None,
    ) -> MasterKelurahan | None:
        master_kelurahan = MasterKelurahan(
            idkelurahan=idkelurahan,
            idkecamatan=idkecamatan,
            nmkelurahan=nmkelurahan,
            alamat=alamat,
            telepon=telepon,
            status=status,
            kdkelurahan=kdkelurahan,
            kodepos=kodepos,
            updated_by=updated_by,
        )
        return self.repository.update(idkelurahan, master_kelurahan)

    def delete(self, idkelurahan: int) -> bool:
        return self.repository.delete(idkelurahan)
