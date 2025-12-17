from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core.database import SessionLocal
from infrastructure.repositories.user_repository_impl import UserRepositoryImpl
from usecases.user_usecase import UserUseCase
from schemas.user_schema import UserCreate, UserResponse

router = APIRouter(prefix="/users", tags=["Users"])

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
    return uc.create_user(
        user.username,
        user.email,
        user.password,
        user.full_name
    )

@router.get("/", response_model=list[UserResponse])
def get_users(uc: UserUseCase = Depends(get_usecase)):
    return uc.get_users()
