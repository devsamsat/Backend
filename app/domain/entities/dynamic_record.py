from dataclasses import dataclass
from datetime import datetime
from typing import Any, Optional


@dataclass
class DynamicRecord:
    id: Optional[int]
    table_name: str
    record_id: str
    payload: dict[str, Any]
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
