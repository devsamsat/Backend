from sqlalchemy.orm import Session
from app.domain.entities.appuser import AppUser
from app.domain.repositories.appuser_repository import AppUserRepository
from app.infrastructure.orm.models import AppUserModel


class AppUserRepositoryImpl(AppUserRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(AppUserModel).all()

    def get_by_id(self, userid: str):
        return self.db.query(AppUserModel).filter(AppUserModel.userid == userid).first()

    def create(self, appuser: AppUser):
        db_record = AppUserModel(**appuser.__dict__)
        self.db.add(db_record)
        self.db.commit()
        self.db.refresh(db_record)
        return db_record

    def update(self, userid: str, appuser: AppUser):
        db_record = self.get_by_id(userid)
        if not db_record:
            return None

        for key, value in appuser.__dict__.items():
            if value is not None and key != "userid":
                setattr(db_record, key, value)

        self.db.commit()
        self.db.refresh(db_record)
        return db_record

    def delete(self, userid: str):
        db_record = self.get_by_id(userid)
        if not db_record:
            return False
        self.db.delete(db_record)
        self.db.commit()
        return True
