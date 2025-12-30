from typing import List

from app.domain.entities.masterbendahara import MasterBendahara
from app.domain.repositories.masterbendahara_repository import MasterBendaharaRepository


class MasterBendaharaUseCase:

    def __init__(self, repository: MasterBendaharaRepository):
        self.repository = repository

    def get_all(self) -> List[MasterBendahara]:
        return self.repository.get_all()

    def get_by_id(self, idbend: int) -> MasterBendahara | None:
        return self.repository.get_by_id(idbend)

    def create(
        self,
        idpegawai: int,
        idbank: int,
        norek: str,
        namarek: str,
        jnsbend: str,
        status: str,
        jabatan: str | None = None,
        pangkat: str | None = None,
        uid: str | None = None,
        koordinator: int | None = None,
        idreknrc: int | None = None,
        telepon: str | None = None,
        ket: str | None = None,
        created_by: str | None = None,
        updated_by: str | None = None,
    ) -> MasterBendahara:
        master_bendahara = MasterBendahara(
            idbend=None,
            idpegawai=idpegawai,
            idbank=idbank,
            norek=norek,
            namarek=namarek,
            jnsbend=jnsbend,
            status=status,
            jabatan=jabatan,
            pangkat=pangkat,
            uid=uid,
            koordinator=koordinator,
            idreknrc=idreknrc,
            telepon=telepon,
            ket=ket,
            created_by=created_by,
            updated_by=updated_by,
        )
        return self.repository.create(master_bendahara)

    def update(
        self,
        idbend: int,
        idpegawai: int | None,
        idbank: int | None,
        norek: str | None,
        namarek: str | None,
        jnsbend: str | None,
        status: str | None,
        jabatan: str | None,
        pangkat: str | None,
        uid: str | None,
        koordinator: int | None,
        idreknrc: int | None,
        telepon: str | None,
        ket: str | None,
        updated_by: str | None,
    ) -> MasterBendahara | None:
        master_bendahara = MasterBendahara(
            idbend=idbend,
            idpegawai=idpegawai,
            idbank=idbank,
            norek=norek,
            namarek=namarek,
            jnsbend=jnsbend,
            status=status,
            jabatan=jabatan,
            pangkat=pangkat,
            uid=uid,
            koordinator=koordinator,
            idreknrc=idreknrc,
            telepon=telepon,
            ket=ket,
            updated_by=updated_by,
        )
        return self.repository.update(idbend, master_bendahara)

    def delete(self, idbend: int) -> bool:
        return self.repository.delete(idbend)
