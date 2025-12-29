from __future__ import annotations

from datetime import date, datetime
from decimal import Decimal
from typing import Any, Dict, Type

from sqlalchemy import and_
from sqlalchemy.orm import Session
from sqlalchemy.sql.sqltypes import (
    Boolean,
    Date,
    DateTime,
    Float,
    Integer,
    Numeric,
)

from app.core.table_constants import CUSTOM_TABLES
from app.domain.repositories.generated_table_repository import GeneratedTableRepository
from app.infrastructure.orm.generated_models import MODEL_REGISTRY
from app.infrastructure.orm.table_registry import TABLE_NAMES


class BaseGeneratedTableRepositoryImpl(GeneratedTableRepository):
    model: Type[Any]

    def __init__(self, db: Session):
        self.db = db
        self.pk_columns = [col.name for col in self.model.__table__.primary_key.columns]

    def get_all(self) -> list[Any]:
        return self.db.query(self.model).all()

    def get_by_id(self, pk_values: dict[str, Any]) -> Any | None:
        query = self.db.query(self.model).filter(self._pk_filter(pk_values))
        return query.first()

    def create(self, entity: Any) -> Any:
        db_obj = self.model(**entity.__dict__)
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update(self, pk_values: dict[str, Any], entity: Any) -> Any | None:
        db_obj = self.get_by_id(pk_values)
        if not db_obj:
            return None
        for key, value in entity.__dict__.items():
            if key in self.pk_columns:
                continue
            if value is not None:
                setattr(db_obj, key, value)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete(self, pk_values: dict[str, Any]) -> bool:
        db_obj = self.get_by_id(pk_values)
        if not db_obj:
            return False
        self.db.delete(db_obj)
        self.db.commit()
        return True

    def _pk_filter(self, pk_values: dict[str, Any]):
        missing = [col for col in self.pk_columns if col not in pk_values]
        if missing:
            missing_cols = ", ".join(missing)
            raise ValueError(f"Missing primary key values: {missing_cols}")
        return and_(
            *[
                getattr(self.model, name)
                == self._coerce_value(self.model.__table__.c[name], pk_values[name])
                for name in self.pk_columns
            ]
        )

    def _coerce_value(self, column, value: Any):
        if value is None:
            return None
        if isinstance(column.type, Integer):
            return int(value)
        if isinstance(column.type, Numeric):
            return Decimal(value)
        if isinstance(column.type, Float):
            return float(value)
        if isinstance(column.type, Boolean):
            return str(value).lower() in {"1", "true", "t", "yes", "y"}
        if isinstance(column.type, Date):
            if isinstance(value, date):
                return value
            return date.fromisoformat(value)
        if isinstance(column.type, DateTime):
            if isinstance(value, datetime):
                return value
            return datetime.fromisoformat(value)
        return value


def _to_camel(name: str) -> str:
    return "".join(part.capitalize() for part in name.split("_"))


REPOSITORY_REGISTRY: Dict[str, Type[BaseGeneratedTableRepositoryImpl]] = {}

for table_name in TABLE_NAMES:
    if table_name in CUSTOM_TABLES:
        continue
    model = MODEL_REGISTRY[table_name]
    class_name = f"{_to_camel(table_name)}Repository"
    REPOSITORY_REGISTRY[table_name] = type(
        class_name,
        (BaseGeneratedTableRepositoryImpl,),
        {"model": model},
    )


def get_repository_class(table_name: str) -> Type[BaseGeneratedTableRepositoryImpl]:
    return REPOSITORY_REGISTRY[table_name]
