from __future__ import annotations

from datetime import date, datetime
from decimal import Decimal
from typing import Any, Optional

from sqlalchemy import and_, delete, insert, select, update
from sqlalchemy.orm import Session
from sqlalchemy.sql.schema import Table
from sqlalchemy.sql.sqltypes import (
    Boolean,
    Date,
    DateTime,
    Float,
    Integer,
    Numeric,
)

from app.domain.entities.table_record import TableRecord
from app.domain.repositories.table_repository import TableRepository
from app.infrastructure.orm.table_registry import get_table


class TableRepositoryImpl(TableRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_all(self, table_name: str) -> list[TableRecord]:
        table = get_table(table_name)
        rows = self.db.execute(select(table)).mappings().all()
        return [self._row_to_record(table, row) for row in rows]

    def get_by_id(self, table_name: str, pk_values: dict[str, Any]) -> Optional[TableRecord]:
        table = get_table(table_name)
        row = self.db.execute(
            select(table).where(self._pk_filter(table, pk_values))
        ).mappings().first()
        if not row:
            return None
        return self._row_to_record(table, row)

    def create(self, table_name: str, data: dict[str, Any]) -> TableRecord:
        table = get_table(table_name)
        result = self.db.execute(insert(table).values(**data))
        self.db.commit()
        pk_values = self._resolve_pk_values(table, data, result.inserted_primary_key)
        if pk_values:
            record = self.get_by_id(table_name, pk_values)
            if record:
                return record
        return TableRecord(table_name=table_name, data=data, primary_key=pk_values or None)

    def update(
        self,
        table_name: str,
        pk_values: dict[str, Any],
        data: dict[str, Any],
    ) -> Optional[TableRecord]:
        table = get_table(table_name)
        result = self.db.execute(
            update(table).where(self._pk_filter(table, pk_values)).values(**data)
        )
        if result.rowcount == 0:
            return None
        self.db.commit()
        return self.get_by_id(table_name, pk_values)

    def delete(self, table_name: str, pk_values: dict[str, Any]) -> bool:
        table = get_table(table_name)
        result = self.db.execute(delete(table).where(self._pk_filter(table, pk_values)))
        self.db.commit()
        return result.rowcount > 0

    def _row_to_record(self, table: Table, row: dict[str, Any]) -> TableRecord:
        pk_values = {col.name: row[col.name] for col in table.primary_key.columns}
        return TableRecord(
            table_name=table.name,
            data=dict(row),
            primary_key=pk_values or None,
        )

    def _pk_filter(self, table: Table, pk_values: dict[str, Any]):
        pk_columns = [col.name for col in table.primary_key.columns]
        missing = [col for col in pk_columns if col not in pk_values]
        if missing:
            missing_cols = ", ".join(missing)
            raise ValueError(f"Missing primary key values: {missing_cols}")
        return and_(
            *[
                table.c[name] == self._coerce_value(table.c[name], pk_values[name])
                for name in pk_columns
            ]
        )

    def _resolve_pk_values(
        self,
        table: Table,
        data: dict[str, Any],
        inserted_pk: list[Any],
    ) -> dict[str, Any]:
        pk_columns = [col.name for col in table.primary_key.columns]
        if not pk_columns:
            return {}
        if inserted_pk:
            return {name: inserted_pk[idx] for idx, name in enumerate(pk_columns)}
        return {name: data.get(name) for name in pk_columns if name in data}

    def _coerce_value(self, column, value: Any):
        if value is None:
            return None
        if isinstance(column.type, (Integer,)):
            return int(value)
        if isinstance(column.type, (Numeric,)):
            return Decimal(value)
        if isinstance(column.type, (Float,)):
            return float(value)
        if isinstance(column.type, (Boolean,)):
            return str(value).lower() in {"1", "true", "t", "yes", "y"}
        if isinstance(column.type, (Date,)):
            if isinstance(value, date):
                return value
            return date.fromisoformat(value)
        if isinstance(column.type, (DateTime,)):
            if isinstance(value, datetime):
                return value
            return datetime.fromisoformat(value)
        return value
