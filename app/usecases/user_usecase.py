from typing import List
from domain.entities.user import User
from domain.repositories.user_repository import UserRepository
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserUseCase:

    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def get_users(self) -> List[User]:
        return self.user_repo.get_all()

    def get_user(self, user_id: int) -> User | None:
        return self.user_repo.get_by_id(user_id)

    def create_user(
        self,
        username: str,
        email: str,
        password: str,
        full_name: str | None
    ) -> User:
        password_hash = pwd_context.hash(password)

        user = User(
            id=None,
            username=username,
            email=email,
            password_hash=password_hash,
            full_name=full_name,
            is_active=True
        )

        return self.user_repo.create(user)

    def update_user(self, user_id: int, user: User):
        return self.user_repo.update(user_id, user)

    def delete_user(self, user_id: int) -> bool:
        return self.user_repo.delete(user_id)
