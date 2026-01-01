from fastapi import FastAPI
from app.core.database import Base, engine
from app.infrastructure.orm.table_registry import create_tables
from app.interfaces.api import (
    appgroupuser,
    appotor,
    approle,
    appuser,
    dynamic_records,
    jnsdok,
    jnsgolongan,
    jnsguna,
    mastertarifnjop,
    masterteks,
    masterupt,
    masteruunjop,
    masterwp,
    masterwpdata,
    transdatakohir,
    transhistpendataan,
    transhistpendataandet,
    transhistpenetapan,
    users,
)
from app.interfaces.api.generated_tables import generate_table_routers

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
app.include_router(jnsgolongan.router)
app.include_router(jnsguna.router)
app.include_router(mastertarifnjop.router)
app.include_router(masterteks.router)
app.include_router(masterupt.router)
app.include_router(masteruunjop.router)
app.include_router(masterwp.router)
app.include_router(masterwpdata.router)
app.include_router(transdatakohir.router)
app.include_router(transhistpendataan.router)
app.include_router(transhistpendataandet.router)
app.include_router(transhistpenetapan.router)

for router in generate_table_routers():
    app.include_router(router)
