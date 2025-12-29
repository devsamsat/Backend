from typing import Any
from datetime import datetime
from pydantic import BaseModel


class DynamicRecordPayload(BaseModel):
    record_id: str
    payload: dict[str, Any]


class DynamicRecordResponse(BaseModel):
    id: int
    table_name: str
    record_id: str
    payload: dict[str, Any]
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
