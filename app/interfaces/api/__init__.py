from __future__ import annotations

from importlib import import_module

from fastapi import FastAPI

from app.core.table_constants import CUSTOM_TABLES
from app.interfaces.api.generated_tables import generate_table_routers


def _load_custom_router(table_name: str):
    module = import_module(f"app.interfaces.api.{table_name}")
    try:
        return module.router
    except AttributeError as exc:
        raise RuntimeError(f"Module app.interfaces.api.{table_name} missing `router`") from exc


def register_table_routers(app: FastAPI) -> None:
    missing_custom: list[str] = []

    for table_name in sorted(CUSTOM_TABLES):
        try:
            app.include_router(_load_custom_router(table_name))
        except Exception:
            missing_custom.append(table_name)

    if missing_custom:
        missing = ", ".join(missing_custom)
        raise RuntimeError(f"Missing or broken custom routers for tables: {missing}")

    for router in generate_table_routers():
        app.include_router(router)
