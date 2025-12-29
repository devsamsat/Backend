from fastapi import FastAPI
from app.core.database import Base, engine
from app.interfaces.api import users

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Clean Architecture Users API")

app.include_router(users.router)
