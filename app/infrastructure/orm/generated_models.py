from __future__ import annotations

import re
from typing import Dict, Type

from app.core.database import Base
from app.core.table_constants import CUSTOM_TABLES
from app.infrastructure.orm.table_registry import TABLE_NAMES, get_table

MODEL_REGISTRY: Dict[str, Type[Base]] = {}


def _to_camel(name: str) -> str:
    parts = re.split(r"[^a-zA-Z0-9]", name)
    return "".join(part.capitalize() for part in parts if part)


for table_name in TABLE_NAMES:
    if table_name in CUSTOM_TABLES:
        continue
    table = get_table(table_name)
    class_name = f"{_to_camel(table_name)}Model"
    MODEL_REGISTRY[table_name] = type(class_name, (Base,), {"__table__": table})
