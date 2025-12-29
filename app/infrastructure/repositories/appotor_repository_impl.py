from sqlalchemy.orm import Session
from app.domain.entities.appotor import AppOtor
from app.domain.repositories.appotor_repository import AppOtorRepository
from app.infrastructure.orm.models import AppOtor as AppOtorModel


class AppOtorRepositoryImpl(AppOtorRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return (
            self.db.query(AppOtorModel)
            .order_by(AppOtorModel.kdgroup.asc(), AppOtorModel.roleid.asc())
            .all()
        )

    def get_by_id(self, kdgroup: str, roleid: str):
        return (
            self.db.query(AppOtorModel)
            .filter(AppOtorModel.kdgroup == kdgroup, AppOtorModel.roleid == roleid)
            .first()
        )

    def create(self, app_otor: AppOtor):
        db_otor = AppOtorModel(**app_otor.__dict__)
        self.db.add(db_otor)
        self.db.commit()
        self.db.refresh(db_otor)
        return db_otor

    def update(self, kdgroup: str, roleid: str, app_otor: AppOtor):
        db_otor = self.get_by_id(kdgroup, roleid)
        if not db_otor:
            return None

        for key, value in app_otor.__dict__.items():
            if key in {"kdgroup", "roleid"}:
                continue
            if value is not None:
                setattr(db_otor, key, value)

        self.db.commit()
        self.db.refresh(db_otor)
        return db_otor

    def delete(self, kdgroup: str, roleid: str):
        db_otor = self.get_by_id(kdgroup, roleid)
        if not db_otor:
            return False
        self.db.delete(db_otor)
        self.db.commit()
        return True
