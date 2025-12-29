from sqlalchemy.orm import Session
from app.domain.entities.approle import AppRole
from app.domain.repositories.approle_repository import AppRoleRepository
from app.infrastructure.orm.models import AppRole as AppRoleModel


class AppRoleRepositoryImpl(AppRoleRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(AppRoleModel).order_by(AppRoleModel.roleid.asc()).all()

    def get_by_id(self, roleid: str):
        return self.db.query(AppRoleModel).filter(AppRoleModel.roleid == roleid).first()

    def create(self, app_role: AppRole):
        db_role = AppRoleModel(**app_role.__dict__)
        self.db.add(db_role)
        self.db.commit()
        self.db.refresh(db_role)
        return db_role

    def update(self, roleid: str, app_role: AppRole):
        db_role = self.get_by_id(roleid)
        if not db_role:
            return None

        for key, value in app_role.__dict__.items():
            if key == "roleid":
                continue
            if value is not None:
                setattr(db_role, key, value)

        self.db.commit()
        self.db.refresh(db_role)
        return db_role

    def delete(self, roleid: str):
        db_role = self.get_by_id(roleid)
        if not db_role:
            return False
        self.db.delete(db_role)
        self.db.commit()
        return True
