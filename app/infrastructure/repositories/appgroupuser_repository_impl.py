from sqlalchemy.orm import Session
from app.domain.entities.appgroupuser import AppGroupUser
from app.domain.repositories.appgroupuser_repository import AppGroupUserRepository
from app.infrastructure.orm.models import AppGroupUserModel


class AppGroupUserRepositoryImpl(AppGroupUserRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(AppGroupUserModel).all()

    def get_by_id(self, kdgroup: str):
        return (
            self.db.query(AppGroupUserModel)
            .filter(AppGroupUserModel.kdgroup == kdgroup)
            .first()
        )

    def create(self, appgroupuser: AppGroupUser):
        db_record = AppGroupUserModel(**appgroupuser.__dict__)
        self.db.add(db_record)
        self.db.commit()
        self.db.refresh(db_record)
        return db_record

    def update(self, kdgroup: str, appgroupuser: AppGroupUser):
        db_record = self.get_by_id(kdgroup)
        if not db_record:
            return None

        for key, value in appgroupuser.__dict__.items():
            if value is not None and key != "kdgroup":
                setattr(db_record, key, value)

        self.db.commit()
        self.db.refresh(db_record)
        return db_record

    def delete(self, kdgroup: str):
        db_record = self.get_by_id(kdgroup)
        if not db_record:
            return False
        self.db.delete(db_record)
        self.db.commit()
        return True
