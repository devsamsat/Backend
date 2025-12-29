from sqlalchemy.orm import Session
from app.domain.entities.appuser import AppUser
from app.domain.repositories.appuser_repository import AppUserRepository
from app.infrastructure.orm.models import AppUser as AppUserModel


class AppUserRepositoryImpl(AppUserRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(AppUserModel).order_by(AppUserModel.userid.asc()).all()

    def get_by_id(self, userid: str):
        return self.db.query(AppUserModel).filter(AppUserModel.userid == userid).first()

    def create(self, app_user: AppUser):
        db_user = AppUserModel(**app_user.__dict__)
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def update(self, userid: str, app_user: AppUser):
        db_user = self.get_by_id(userid)
        if not db_user:
            return None

        for key, value in app_user.__dict__.items():
            if key == "userid":
                continue
            if value is not None:
                setattr(db_user, key, value)

        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def delete(self, userid: str):
        db_user = self.get_by_id(userid)
        if not db_user:
            return False
        self.db.delete(db_user)
        self.db.commit()
        return True
