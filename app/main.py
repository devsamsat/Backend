from fastapi import FastAPI
from app.core.database import Base, engine
from app.infrastructure.orm.table_registry import create_tables
from app.interfaces.api import register_table_routers

Base.metadata.create_all(bind=engine)
create_tables()

app = FastAPI(
    title="Clean Architecture Users API",
    docs_url="/",
    redoc_url=None,
)

register_table_routers(app)
