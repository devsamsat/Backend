from dataclasses import dataclass
from typing import Any


@dataclass
class TableRecord:
    table_name: str
    data: dict[str, Any]
    primary_key: dict[str, Any] | None = None
