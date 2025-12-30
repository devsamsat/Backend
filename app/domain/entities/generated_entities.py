from __future__ import annotations

from dataclasses import field, make_dataclass
from typing import Any, Dict, Optional, Type

from app.core.table_constants import CUSTOM_TABLES
from app.infrastructure.orm.table_registry import TABLE_NAMES, get_table

ENTITY_REGISTRY: Dict[str, Type[Any]] = {}


def _python_type(column) -> type:
    try:
        return column.type.python_type
    except (AttributeError, NotImplementedError):
        return Any


for table_name in TABLE_NAMES:
    if table_name in CUSTOM_TABLES:
        continue
    table = get_table(table_name)
    fields = []
    for column in table.columns:
        py_type = _python_type(column)
        fields.append((column.name, Optional[py_type], field(default=None)))
    class_name = "".join(part.capitalize() for part in table_name.split("_"))
    ENTITY_REGISTRY[table_name] = make_dataclass(
        class_name,
        fields,
    )
