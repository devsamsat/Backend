from __future__ import annotations

from fastapi import FastAPI

from app.core.table_constants import CUSTOM_TABLES
from app.interfaces.api import (
    appgroupuser,
    appotor,
    approle,
    appuser,
    dynamic_records,
    jnsdok,
    jnshist,
    jnsjr,
    jnskatkendaraan,
    jnskendaraan,
    jnsmilik,
    jnspajak,
    jnsplat,
    jnsprogresif,
    jnsranmor,
    jnsgolongan,
    jnsguna,
    users,
)
from app.interfaces.api.generated_tables import generate_table_routers


CUSTOM_ROUTER_REGISTRY = {
    "users": users.router,
    "dynamic_records": dynamic_records.router,
    "appgroupuser": appgroupuser.router,
    "appotor": appotor.router,
    "approle": approle.router,
    "appuser": appuser.router,
    "jnsdok": jnsdok.router,
    "jnshist": jnshist.router,
    "jnsjr": jnsjr.router,
    "jnskatkendaraan": jnskatkendaraan.router,
    "jnskendaraan": jnskendaraan.router,
    "jnsmilik": jnsmilik.router,
    "jnspajak": jnspajak.router,
    "jnsplat": jnsplat.router,
    "jnsprogresif": jnsprogresif.router,
    "jnsranmor": jnsranmor.router,
    "jnsgolongan": jnsgolongan.router,
    "jnsguna": jnsguna.router,
}


def register_table_routers(app: FastAPI) -> None:
    missing_custom = CUSTOM_TABLES - CUSTOM_ROUTER_REGISTRY.keys()
    if missing_custom:
        missing = ", ".join(sorted(missing_custom))
        raise RuntimeError(f"Missing custom routers for tables: {missing}")

    for router in CUSTOM_ROUTER_REGISTRY.values():
        app.include_router(router)

    for router in generate_table_routers():
        app.include_router(router)
