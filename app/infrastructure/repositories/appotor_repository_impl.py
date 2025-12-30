from sqlalchemy.orm import Session
from app.domain.entities.appotor import AppOtor
from app.domain.repositories.appotor_repository import AppOtorRepository
from app.infrastructure.orm.models import AppOtorModel


class AppOtorRepositoryImpl(AppOtorRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(AppOtorModel).all()

    def get_by_id(self, kdgroup: str, roleid: str):
        return (
            self.db.query(AppOtorModel)
            .filter(
                AppOtorModel.kdgroup == kdgroup,
                AppOtorModel.roleid == roleid,
            )
            .first()
        )

    def create(self, appotor: AppOtor):
        db_record = AppOtorModel(**appotor.__dict__)
        self.db.add(db_record)
        self.db.commit()
        self.db.refresh(db_record)
        return db_record

    def update(self, kdgroup: str, roleid: str, appotor: AppOtor):
        db_record = self.get_by_id(kdgroup, roleid)
        if not db_record:
            return None

        for key, value in appotor.__dict__.items():
            if value is not None and key not in {"kdgroup", "roleid"}:
                setattr(db_record, key, value)

        self.db.commit()
        self.db.refresh(db_record)
        return db_record

    def delete(self, kdgroup: str, roleid: str):
        db_record = self.get_by_id(kdgroup, roleid)
        if not db_record:
            return False
        self.db.delete(db_record)
        self.db.commit()
        return True
