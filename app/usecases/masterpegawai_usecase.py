from typing import List

from app.domain.entities.masterpegawai import MasterPegawai
from app.domain.repositories.masterpegawai_repository import MasterPegawaiRepository


class MasterPegawaiUseCase:

    def __init__(self, repository: MasterPegawaiRepository):
        self.repository = repository

    def get_all(self) -> List[MasterPegawai]:
        return self.repository.get_all()

    def get_by_id(self, idpegawai: int) -> MasterPegawai | None:
        return self.repository.get_by_id(idpegawai)

    def create(
        self,
        idktp: int | None,
        nip: str,
        nik: str | None,
        nama: str,
        idupt: int,
        status: str,
        jabatan: str | None,
        pangkat: str | None,
        golongan: str | None,
        uid: str | None,
        telepon: str | None,
        created_by: str | None,
        updated_by: str | None,
    ) -> MasterPegawai:
        master_pegawai = MasterPegawai(
            idpegawai=None,
            idktp=idktp,
            nip=nip,
            nik=nik,
            nama=nama,
            idupt=idupt,
            status=status,
            jabatan=jabatan,
            pangkat=pangkat,
            golongan=golongan,
            uid=uid,
            telepon=telepon,
            created_by=created_by,
            updated_by=updated_by,
        )
        return self.repository.create(master_pegawai)

    def update(
        self,
        idpegawai: int,
        idktp: int | None,
        nip: str | None,
        nik: str | None,
        nama: str | None,
        idupt: int | None,
        status: str | None,
        jabatan: str | None,
        pangkat: str | None,
        golongan: str | None,
        uid: str | None,
        telepon: str | None,
        updated_by: str | None,
    ) -> MasterPegawai | None:
        master_pegawai = MasterPegawai(
            idpegawai=idpegawai,
            idktp=idktp,
            nip=nip,
            nik=nik,
            nama=nama,
            idupt=idupt,
            status=status,
            jabatan=jabatan,
            pangkat=pangkat,
            golongan=golongan,
            uid=uid,
            telepon=telepon,
            updated_by=updated_by,
        )
        return self.repository.update(idpegawai, master_pegawai)

    def delete(self, idpegawai: int) -> bool:
        return self.repository.delete(idpegawai)
