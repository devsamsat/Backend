from typing import List

from app.domain.entities.transwpdatafile import TransWpDataFile
from app.domain.repositories.transwpdatafile_repository import TransWpDataFileRepository


class TransWpDataFileUseCase:

    def __init__(self, repository: TransWpDataFileRepository):
        self.repository = repository

    def get_all(self) -> List[TransWpDataFile]:
        return self.repository.get_all()

    def get_by_id(self, idfile: int) -> TransWpDataFile | None:
        return self.repository.get_by_id(idfile)

    def create(
        self,
        idtwpdata: int,
        namafile: str | None = None,
        direktory: str | None = None,
        extension: str | None = None,
        size: int | None = None,
        url: str | None = None,
        created_by: str | None = None,
        updated_by: str | None = None,
    ) -> TransWpDataFile:
        trans_wpdatafile = TransWpDataFile(
            idfile=None,
            idtwpdata=idtwpdata,
            namafile=namafile,
            direktory=direktory,
            extension=extension,
            size=size,
            url=url,
            created_by=created_by,
            updated_by=updated_by,
        )
        return self.repository.create(trans_wpdatafile)

    def update(
        self,
        idfile: int,
        idtwpdata: int | None,
        namafile: str | None,
        direktory: str | None,
        extension: str | None,
        size: int | None,
        url: str | None,
        updated_by: str | None,
    ) -> TransWpDataFile | None:
        trans_wpdatafile = TransWpDataFile(
            idfile=idfile,
            idtwpdata=idtwpdata,
            namafile=namafile,
            direktory=direktory,
            extension=extension,
            size=size,
            url=url,
            updated_by=updated_by,
        )
        return self.repository.update(idfile, trans_wpdatafile)

    def delete(self, idfile: int) -> bool:
        return self.repository.delete(idfile)
