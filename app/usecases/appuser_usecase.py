from typing import List
from app.domain.entities.appuser import AppUser
from app.domain.repositories.appuser_repository import AppUserRepository


class AppUserUseCase:

    def __init__(self, repository: AppUserRepository):
        self.repository = repository

    def get_all(self) -> List[AppUser]:
        return self.repository.get_all()

    def get_by_id(self, userid: str) -> AppUser | None:
        return self.repository.get_by_id(userid)

    def create(
        self,
        userid: str,
        kdtahap: str,
        kdgroup: str,
        idupt: int | None,
        pwd: str | None,
        idpeg: int | None,
        nik: str | None,
        nama: str | None,
        email: str | None,
        created_by: str | None,
        updated_by: str | None,
    ) -> AppUser:
        app_user = AppUser(
            userid=userid,
            kdtahap=kdtahap,
            kdgroup=kdgroup,
            idupt=idupt,
            pwd=pwd,
            idpeg=idpeg,
            nik=nik,
            nama=nama,
            email=email,
            created_by=created_by,
            updated_by=updated_by,
        )
        return self.repository.create(app_user)

    def update(
        self,
        userid: str,
        kdtahap: str | None,
        kdgroup: str | None,
        idupt: int | None,
        pwd: str | None,
        idpeg: int | None,
        nik: str | None,
        nama: str | None,
        email: str | None,
        updated_by: str | None,
    ) -> AppUser | None:
        app_user = AppUser(
            userid=userid,
            kdtahap=kdtahap,
            kdgroup=kdgroup,
            idupt=idupt,
            pwd=pwd,
            idpeg=idpeg,
            nik=nik,
            nama=nama,
            email=email,
            updated_by=updated_by,
        )
        return self.repository.update(userid, app_user)

    def delete(self, userid: str) -> bool:
        return self.repository.delete(userid)
