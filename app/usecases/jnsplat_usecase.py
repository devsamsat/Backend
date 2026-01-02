from typing import List

from app.domain.entities.jnsplat import JnsPlat
from app.domain.repositories.jnsplat_repository import JnsPlatRepository


class JnsPlatUseCase:

    def __init__(self, repository: JnsPlatRepository):
        self.repository = repository

    def get_all(self) -> List[JnsPlat]:
        return self.repository.get_all()

    def get_by_id(self, kdplat: str) -> JnsPlat | None:
        return self.repository.get_by_id(kdplat)

    def create(
        self,
        kdplat: str,
        plat: str,
        pu: str,
        platjr: int,
        numpkb: float,
        numbbn1: float,
        numbbn2: float,
        umorg: float,
        umbrg: float,
        dnumpkb: float,
        dnumbbn: float,
        dumorg: float,
        dumbrg: float,
        abpkb: float,
        abbbn1: float,
        abbbn2: float,
        numfiskal: float,
        snid: str,
        opspkb: float,
        opsbbn: float,
        opsnumpkb: float,
        opsnumbbn1: float,
        opsnumbbn2: float,
        opsdnumpkb: float,
        opsdnumbbn: float,
        minnumpkb: float,
        minnumbbn1: float,
        minnumbbn2: float,
        created_by: str | None,
        updated_by: str | None,
    ) -> JnsPlat:
        jns_plat = JnsPlat(
            kdplat=kdplat,
            plat=plat,
            pu=pu,
            platjr=platjr,
            numpkb=numpkb,
            numbbn1=numbbn1,
            numbbn2=numbbn2,
            umorg=umorg,
            umbrg=umbrg,
            dnumpkb=dnumpkb,
            dnumbbn=dnumbbn,
            dumorg=dumorg,
            dumbrg=dumbrg,
            abpkb=abpkb,
            abbbn1=abbbn1,
            abbbn2=abbbn2,
            numfiskal=numfiskal,
            snid=snid,
            opspkb=opspkb,
            opsbbn=opsbbn,
            opsnumpkb=opsnumpkb,
            opsnumbbn1=opsnumbbn1,
            opsnumbbn2=opsnumbbn2,
            opsdnumpkb=opsdnumpkb,
            opsdnumbbn=opsdnumbbn,
            minnumpkb=minnumpkb,
            minnumbbn1=minnumbbn1,
            minnumbbn2=minnumbbn2,
            created_by=created_by,
            updated_by=updated_by,
        )
        return self.repository.create(jns_plat)

    def update(
        self,
        kdplat: str,
        plat: str | None,
        pu: str | None,
        platjr: int | None,
        numpkb: float | None,
        numbbn1: float | None,
        numbbn2: float | None,
        umorg: float | None,
        umbrg: float | None,
        dnumpkb: float | None,
        dnumbbn: float | None,
        dumorg: float | None,
        dumbrg: float | None,
        abpkb: float | None,
        abbbn1: float | None,
        abbbn2: float | None,
        numfiskal: float | None,
        snid: str | None,
        opspkb: float | None,
        opsbbn: float | None,
        opsnumpkb: float | None,
        opsnumbbn1: float | None,
        opsnumbbn2: float | None,
        opsdnumpkb: float | None,
        opsdnumbbn: float | None,
        minnumpkb: float | None,
        minnumbbn1: float | None,
        minnumbbn2: float | None,
        updated_by: str | None,
    ) -> JnsPlat | None:
        jns_plat = JnsPlat(
            kdplat=kdplat,
            plat=plat,
            pu=pu,
            platjr=platjr,
            numpkb=numpkb,
            numbbn1=numbbn1,
            numbbn2=numbbn2,
            umorg=umorg,
            umbrg=umbrg,
            dnumpkb=dnumpkb,
            dnumbbn=dnumbbn,
            dumorg=dumorg,
            dumbrg=dumbrg,
            abpkb=abpkb,
            abbbn1=abbbn1,
            abbbn2=abbbn2,
            numfiskal=numfiskal,
            snid=snid,
            opspkb=opspkb,
            opsbbn=opsbbn,
            opsnumpkb=opsnumpkb,
            opsnumbbn1=opsnumbbn1,
            opsnumbbn2=opsnumbbn2,
            opsdnumpkb=opsdnumpkb,
            opsdnumbbn=opsdnumbbn,
            minnumpkb=minnumpkb,
            minnumbbn1=minnumbbn1,
            minnumbbn2=minnumbbn2,
            updated_by=updated_by,
        )
        return self.repository.update(kdplat, jns_plat)

    def delete(self, kdplat: str) -> bool:
        return self.repository.delete(kdplat)
