from fastapi import FastAPI
from core.database import Base, engine
from interfaces.api import users

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Clean Architecture Users API")

app.include_router(users.router)
