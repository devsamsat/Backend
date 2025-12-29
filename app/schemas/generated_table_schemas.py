from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, Optional, Type

from pydantic import BaseModel, ConfigDict, create_model

from app.core.table_constants import CUSTOM_TABLES
from app.infrastructure.orm.table_registry import TABLE_NAMES, get_table


@dataclass(frozen=True)
class TableSchemas:
    create: Type[BaseModel]
    update: Type[BaseModel]
    response: Type[BaseModel]


def _python_type(column) -> type:
    try:
        return column.type.python_type
    except (AttributeError, NotImplementedError):
        return Any


def _optional_for_column(column) -> bool:
    if column.nullable:
        return True
    if column.default is not None or column.server_default is not None:
        return True
    if column.autoincrement not in (None, False, "auto"):
        return True
    return False


def _create_response_model(name: str, fields: dict[str, tuple[type, Any]]):
    return create_model(
        name,
        __config__=ConfigDict(from_attributes=True),
        **fields,
    )


SCHEMA_REGISTRY: Dict[str, TableSchemas] = {}

for table_name in TABLE_NAMES:
    if table_name in CUSTOM_TABLES:
        continue
    table = get_table(table_name)
    create_fields: dict[str, tuple[type, Any]] = {}
    update_fields: dict[str, tuple[type, Any]] = {}
    response_fields: dict[str, tuple[type, Any]] = {}

    pk_columns = {col.name for col in table.primary_key.columns}

    for column in table.columns:
        py_type = _python_type(column)
        optional = _optional_for_column(column)
        if optional:
            type_hint = Optional[py_type]
            create_fields[column.name] = (type_hint, None)
        else:
            create_fields[column.name] = (py_type, ...)
        if column.name not in pk_columns:
            update_fields[column.name] = (Optional[py_type], None)
        if optional:
            response_fields[column.name] = (Optional[py_type], None)
        else:
            response_fields[column.name] = (py_type, ...)

    class_name = "".join(part.capitalize() for part in table_name.split("_"))
    create_model_name = f"{class_name}Create"
    update_model_name = f"{class_name}Update"
    response_model_name = f"{class_name}Response"

    create_model_cls = create_model(create_model_name, **create_fields)
    update_model_cls = create_model(update_model_name, **update_fields)
    response_model_cls = _create_response_model(response_model_name, response_fields)

    SCHEMA_REGISTRY[table_name] = TableSchemas(
        create=create_model_cls,
        update=update_model_cls,
        response=response_model_cls,
    )
