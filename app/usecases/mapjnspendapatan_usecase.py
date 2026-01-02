from typing import List

from app.domain.entities.mapjnspendapatan import MapJnsPendapatan
from app.domain.repositories.mapjnspendapatan_repository import MapJnsPendapatanRepository


class MapJnsPendapatanUseCase:

    def __init__(self, repository: MapJnsPendapatanRepository):
        self.repository = repository

    def get_all(self) -> List[MapJnsPendapatan]:
        return self.repository.get_all()

    def get_by_id(self, idmapjnsd: int) -> MapJnsPendapatan | None:
        return self.repository.get_by_id(idmapjnsd)

    def create(
        self,
        nmjnspendapatan: str,
        idrekpkb: int | None,
        idrekbbnkb: int | None,
        idrekopsenpkb: int | None,
        idrekopsenbbnkb: int | None,
        idrekpnbp: int | None,
        keterangan: str | None,
        created_by: str | None,
        updated_by: str | None,
    ) -> MapJnsPendapatan:
        map_jns_pendapatan = MapJnsPendapatan(
            idmapjnsd=None,
            nmjnspendapatan=nmjnspendapatan,
            idrekpkb=idrekpkb,
            idrekbbnkb=idrekbbnkb,
            idrekopsenpkb=idrekopsenpkb,
            idrekopsenbbnkb=idrekopsenbbnkb,
            idrekpnbp=idrekpnbp,
            keterangan=keterangan,
            created_by=created_by,
            updated_by=updated_by,
        )
        return self.repository.create(map_jns_pendapatan)

    def update(
        self,
        idmapjnsd: int,
        nmjnspendapatan: str | None,
        idrekpkb: int | None,
        idrekbbnkb: int | None,
        idrekopsenpkb: int | None,
        idrekopsenbbnkb: int | None,
        idrekpnbp: int | None,
        keterangan: str | None,
        updated_by: str | None,
    ) -> MapJnsPendapatan | None:
        map_jns_pendapatan = MapJnsPendapatan(
            idmapjnsd=idmapjnsd,
            nmjnspendapatan=nmjnspendapatan,
            idrekpkb=idrekpkb,
            idrekbbnkb=idrekbbnkb,
            idrekopsenpkb=idrekopsenpkb,
            idrekopsenbbnkb=idrekopsenbbnkb,
            idrekpnbp=idrekpnbp,
            keterangan=keterangan,
            updated_by=updated_by,
        )
        return self.repository.update(idmapjnsd, map_jns_pendapatan)

    def delete(self, idmapjnsd: int) -> bool:
        return self.repository.delete(idmapjnsd)
