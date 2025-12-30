from typing import List

from app.domain.entities.masterflow import MasterFlow
from app.domain.repositories.masterflow_repository import MasterFlowRepository


class MasterFlowUseCase:

    def __init__(self, repository: MasterFlowRepository):
        self.repository = repository

    def get_all(self) -> List[MasterFlow]:
        return self.repository.get_all()

    def get_by_id(self, kdflow: str) -> MasterFlow | None:
        return self.repository.get_by_id(kdflow)

    def create(
        self,
        kdflow: str,
        nmflow: str,
        pkb: str | None = None,
        bbn1: str | None = None,
        bbn2: str | None = None,
        swd: str | None = None,
        atbkend: str | None = None,
        flowjr: str | None = None,
        stnkbaru: str | None = None,
        tnkb: str | None = None,
        sahstnk: str | None = None,
        perpanjangstnk: str | None = None,
        potongan: str | None = None,
        bataslayanan: int | None = None,
        satuan: str | None = None,
        status: str | None = None,
        created_by: str | None = None,
        updated_by: str | None = None,
    ) -> MasterFlow:
        master_flow = MasterFlow(
            kdflow=kdflow,
            nmflow=nmflow,
            pkb=pkb,
            bbn1=bbn1,
            bbn2=bbn2,
            swd=swd,
            atbkend=atbkend,
            flowjr=flowjr,
            stnkbaru=stnkbaru,
            tnkb=tnkb,
            sahstnk=sahstnk,
            perpanjangstnk=perpanjangstnk,
            potongan=potongan,
            bataslayanan=bataslayanan,
            satuan=satuan,
            status=status,
            created_by=created_by,
            updated_by=updated_by,
        )
        return self.repository.create(master_flow)

    def update(
        self,
        kdflow: str,
        nmflow: str | None,
        pkb: str | None,
        bbn1: str | None,
        bbn2: str | None,
        swd: str | None,
        atbkend: str | None,
        flowjr: str | None,
        stnkbaru: str | None,
        tnkb: str | None,
        sahstnk: str | None,
        perpanjangstnk: str | None,
        potongan: str | None,
        bataslayanan: int | None,
        satuan: str | None,
        status: str | None,
        updated_by: str | None,
    ) -> MasterFlow | None:
        master_flow = MasterFlow(
            kdflow=kdflow,
            nmflow=nmflow,
            pkb=pkb,
            bbn1=bbn1,
            bbn2=bbn2,
            swd=swd,
            atbkend=atbkend,
            flowjr=flowjr,
            stnkbaru=stnkbaru,
            tnkb=tnkb,
            sahstnk=sahstnk,
            perpanjangstnk=perpanjangstnk,
            potongan=potongan,
            bataslayanan=bataslayanan,
            satuan=satuan,
            status=status,
            updated_by=updated_by,
        )
        return self.repository.update(kdflow, master_flow)

    def delete(self, kdflow: str) -> bool:
        return self.repository.delete(kdflow)
