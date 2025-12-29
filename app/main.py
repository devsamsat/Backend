from fastapi import FastAPI
from app.core.database import Base, engine
from app.infrastructure.orm.table_registry import TABLE_NAMES, create_tables
from app.interfaces.api.table_router import create_table_router
from app.interfaces.api import (
    appgroupuser,
    appotor,
    approle,
    appuser,
    dynamic_records,
    jnsdok,
    users,
)

Base.metadata.create_all(bind=engine)
create_tables()

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
app.include_router(jnsdok.router)

custom_table_routes = {
    "users",
    "dynamic_records",
    "appgroupuser",
    "appotor",
    "approle",
    "appuser",
    "jnsdok",
}

for table_name in TABLE_NAMES:
    if table_name in custom_table_routes:
        continue
    app.include_router(create_table_router(table_name))
