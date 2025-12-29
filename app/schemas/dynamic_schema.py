from typing import Any
from datetime import datetime
import json
from pydantic import BaseModel, field_validator


class DynamicRecordCreate(BaseModel):
    table_name: str
    record_id: str
    payload: dict[str, Any]


class DynamicRecordUpdate(BaseModel):
    table_name: str | None = None
    record_id: str | None = None
    payload: dict[str, Any] | None = None


class DynamicRecordResponse(BaseModel):
    id: int
    table_name: str
    record_id: str
    payload: dict[str, Any]
    created_at: datetime
    updated_at: datetime

    @field_validator("payload", mode="before")
    @classmethod
    def parse_payload(cls, value: Any) -> dict[str, Any]:
        if isinstance(value, str):
            return json.loads(value)
        return value

    class Config:
        from_attributes = True
