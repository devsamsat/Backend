from abc import ABC, abstractmethod
from typing import List, Optional

from app.domain.entities.masterpegawai import MasterPegawai


class MasterPegawaiRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[MasterPegawai]:
        pass

    @abstractmethod
    def get_by_id(self, idpegawai: int) -> Optional[MasterPegawai]:
        pass

    @abstractmethod
    def create(self, master_pegawai: MasterPegawai) -> MasterPegawai:
        pass

    @abstractmethod
    def update(self, idpegawai: int, master_pegawai: MasterPegawai) -> Optional[MasterPegawai]:
        pass

    @abstractmethod
    def delete(self, idpegawai: int) -> bool:
        pass
