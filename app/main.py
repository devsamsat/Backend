from fastapi import FastAPI
from app.core.database import Base, engine
from app.interfaces.api import (
    appgroupuser,
    appotor,
    approle,
    appuser,
    dynamic_records,
    users,
)

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Clean Architecture Users API",
    docs_url="/",
    redoc_url=None,
)

app.include_router(users.router)
app.include_router(dynamic_records.router)
app.include_router(appgroupuser.router)
app.include_router(appotor.router)
app.include_router(approle.router)
app.include_router(appuser.router)
