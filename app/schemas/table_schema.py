from typing import Any

from pydantic import BaseModel


class TableRecordCreate(BaseModel):
    data: dict[str, Any]


class TableRecordUpdate(BaseModel):
    data: dict[str, Any]


class TableRecordResponse(BaseModel):
    data: dict[str, Any]
    primary_key: dict[str, Any] | None = None

    class Config:
        from_attributes = True
