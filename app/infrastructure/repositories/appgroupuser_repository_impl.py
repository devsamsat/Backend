from sqlalchemy.orm import Session
from app.domain.entities.appgroupuser import AppGroupUser
from app.domain.repositories.appgroupuser_repository import AppGroupUserRepository
from app.infrastructure.orm.models import AppGroupUser as AppGroupUserModel


class AppGroupUserRepositoryImpl(AppGroupUserRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(AppGroupUserModel).order_by(AppGroupUserModel.kdgroup.asc()).all()

    def get_by_id(self, kdgroup: str):
        return self.db.query(AppGroupUserModel).filter(AppGroupUserModel.kdgroup == kdgroup).first()

    def create(self, group_user: AppGroupUser):
        db_group_user = AppGroupUserModel(**group_user.__dict__)
        self.db.add(db_group_user)
        self.db.commit()
        self.db.refresh(db_group_user)
        return db_group_user

    def update(self, kdgroup: str, group_user: AppGroupUser):
        db_group_user = self.get_by_id(kdgroup)
        if not db_group_user:
            return None

        for key, value in group_user.__dict__.items():
            if key == "kdgroup":
                continue
            if value is not None:
                setattr(db_group_user, key, value)

        self.db.commit()
        self.db.refresh(db_group_user)
        return db_group_user

    def delete(self, kdgroup: str):
        db_group_user = self.get_by_id(kdgroup)
        if not db_group_user:
            return False
        self.db.delete(db_group_user)
        self.db.commit()
        return True
