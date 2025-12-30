from typing import List
from app.domain.entities.user import User
from app.domain.repositories.user_repository import UserRepository
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class UserUseCase:

    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def get_all(self) -> List[User]:
        return self.user_repo.get_all()

    def get_by_id(self, user_id: int) -> User | None:
        return self.user_repo.get_by_id(user_id)

    def hash_password(self, password: str) -> str:
        return pwd_context.hash(password)

    def create(
        self,
        username: str,
        email: str,
        password: str,
        full_name: str | None,
    ) -> User:
        password_hash = self.hash_password(password)

        user = User(
            id=None,
            username=username,
            email=email,
            password_hash=password_hash,
            full_name=full_name,
            is_active=True,
        )

        return self.user_repo.create(user)

    def update(self, user_id: int, user: User):
        return self.user_repo.update(user_id, user)

    def delete(self, user_id: int) -> bool:
        return self.user_repo.delete(user_id)

    def get_users(self) -> List[User]:
        return self.get_all()

    def get_user(self, user_id: int) -> User | None:
        return self.get_by_id(user_id)

    def create_user(
        self,
        username: str,
        email: str,
        password: str,
        full_name: str | None,
    ) -> User:
        return self.create(username, email, password, full_name)

    def update_user(self, user_id: int, user: User):
        return self.update(user_id, user)

    def delete_user(self, user_id: int) -> bool:
        return self.delete(user_id)
