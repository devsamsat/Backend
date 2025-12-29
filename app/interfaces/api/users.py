from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.domain.entities.user import User
from app.infrastructure.repositories.user_repository_impl import UserRepositoryImpl
from app.usecases.user_usecase import UserUseCase
from app.schemas.user_schema import UserCreate, UserResponse, UserUpdate

router = APIRouter(prefix="/api/v1/users", tags=["Users"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_usecase(db: Session = Depends(get_db)):
    repo = UserRepositoryImpl(db)
    return UserUseCase(repo)


@router.post("/", response_model=UserResponse)
def create_user(user: UserCreate, uc: UserUseCase = Depends(get_usecase)):
    return uc.create(
        user.username,
        user.email,
        user.password,
        user.full_name,
    )


@router.get("/", response_model=list[UserResponse])
def get_users(uc: UserUseCase = Depends(get_usecase)):
    return uc.get_all()


@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, uc: UserUseCase = Depends(get_usecase)):
    user = uc.get_by_id(user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user


@router.put("/{user_id}", response_model=UserResponse)
def update_user(
    user_id: int,
    user: UserUpdate,
    uc: UserUseCase = Depends(get_usecase),
):
    password_hash = None
    if user.password is not None:
        password_hash = uc.hash_password(user.password)

    update_payload = User(
        id=user_id,
        username=user.username,
        email=user.email,
        password_hash=password_hash,
        full_name=user.full_name,
        is_active=user.is_active,
    )

    updated = uc.update(user_id, update_payload)
    if not updated:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return updated


@router.delete("/{user_id}")
def delete_user(user_id: int, uc: UserUseCase = Depends(get_usecase)):
    deleted = uc.delete(user_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return {"message": "Deleted"}
