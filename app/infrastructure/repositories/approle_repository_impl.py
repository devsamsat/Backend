from sqlalchemy.orm import Session
from app.domain.entities.approle import AppRole
from app.domain.repositories.approle_repository import AppRoleRepository
from app.infrastructure.orm.models import AppRoleModel


class AppRoleRepositoryImpl(AppRoleRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(AppRoleModel).all()

    def get_by_id(self, roleid: str):
        return (
            self.db.query(AppRoleModel)
            .filter(AppRoleModel.roleid == roleid)
            .first()
        )

    def create(self, approle: AppRole):
        db_record = AppRoleModel(**approle.__dict__)
        self.db.add(db_record)
        self.db.commit()
        self.db.refresh(db_record)
        return db_record

    def update(self, roleid: str, approle: AppRole):
        db_record = self.get_by_id(roleid)
        if not db_record:
            return None

        for key, value in approle.__dict__.items():
            if value is not None and key != "roleid":
                setattr(db_record, key, value)

        self.db.commit()
        self.db.refresh(db_record)
        return db_record

    def delete(self, roleid: str):
        db_record = self.get_by_id(roleid)
        if not db_record:
            return False
        self.db.delete(db_record)
        self.db.commit()
        return True
