from sqlalchemy.orm import Session
from domain.entities.user import User
from domain.repositories.user_repository import UserRepository
from infrastructure.orm.models import UserModel

class UserRepositoryImpl(UserRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(UserModel).all()

    def get_by_id(self, user_id: int):
        return self.db.query(UserModel).filter(UserModel.id == user_id).first()

    def create(self, user: User):
        db_user = UserModel(**user.__dict__)
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def update(self, user_id: int, user: User):
        db_user = self.get_by_id(user_id)
        if not db_user:
            return None

        for key, value in user.__dict__.items():
            if value is not None:
                setattr(db_user, key, value)

        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def delete(self, user_id: int):
        db_user = self.get_by_id(user_id)
        if not db_user:
            return False
        self.db.delete(db_user)
        self.db.commit()
        return True
