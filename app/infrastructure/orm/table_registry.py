from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
from typing import Dict, Iterable, List

from sqlalchemy import (
    BigInteger,
    Boolean,
    Column,
    Date,
    DateTime,
    Float,
    Integer,
    MetaData,
    Numeric,
    String,
    Table,
    Text,
)

from app.core.database import engine

SQL_PATH = Path(__file__).resolve().parents[3] / "db" / "V@LIDSAMSAT.sql"


@dataclass(frozen=True)
class TableDefinition:
    name: str
    columns: List[Column]


_METADATA = MetaData()
_TABLES: Dict[str, Table] = {}


def _parse_primary_keys(sql_text: str) -> Dict[str, List[str]]:
    pk_map: Dict[str, List[str]] = {}
    pattern = re.compile(
        r"ALTER TABLE public\.(?P<table>\w+)\s+ADD CONSTRAINT .*?PRIMARY KEY \((?P<cols>[^)]+)\)",
        re.IGNORECASE,
    )
    for match in pattern.finditer(sql_text):
        table = match.group("table")
        cols = [col.strip() for col in match.group("cols").split(",")]
        pk_map[table] = cols
    return pk_map


def _map_type(type_str: str):
    normalized = type_str.strip().lower()
    if normalized.startswith("character varying") or normalized.startswith("varchar"):
        length_match = re.search(r"\((\d+)\)", normalized)
        length = int(length_match.group(1)) if length_match else None
        return String(length) if length else String()
    if normalized.startswith("character") or normalized.startswith("char"):
        length_match = re.search(r"\((\d+)\)", normalized)
        length = int(length_match.group(1)) if length_match else None
        return String(length) if length else String()
    if normalized.startswith("text"):
        return Text()
    if normalized.startswith("bigint"):
        return BigInteger()
    if normalized.startswith("integer") or normalized == "int":
        return Integer()
    if normalized.startswith("smallint"):
        return Integer()
    if normalized.startswith("numeric") or normalized.startswith("decimal"):
        length_match = re.search(r"\((\d+),(\d+)\)", normalized)
        if length_match:
            return Numeric(int(length_match.group(1)), int(length_match.group(2)))
        return Numeric()
    if normalized.startswith("double precision") or normalized.startswith("real"):
        return Float()
    if normalized.startswith("boolean"):
        return Boolean()
    if "timestamp" in normalized:
        return DateTime(timezone="with time zone" in normalized or "timestamptz" in normalized)
    if normalized.startswith("date"):
        return Date()
    return Text()


def _parse_columns(block: str, pk_cols: Iterable[str]) -> List[Column]:
    columns: List[Column] = []
    pk_set = set(pk_cols)
    for line in block.splitlines():
        line = line.strip().rstrip(",")
        if not line or line.startswith("--"):
            continue
        if line.upper().startswith("CONSTRAINT"):
            continue
        tokens = line.split()
        if not tokens:
            continue
        col_name = tokens[0]
        if col_name.startswith("\"") and col_name.endswith("\""):
            col_name = col_name[1:-1]
        type_tokens = []
        for token in tokens[1:]:
            upper = token.upper()
            if upper in {"NOT", "NULL", "DEFAULT", "CONSTRAINT", "PRIMARY", "REFERENCES"}:
                break
            type_tokens.append(token)
        type_str = " ".join(type_tokens)
        nullable = "NOT NULL" not in line.upper()
        columns.append(
            Column(
                col_name,
                _map_type(type_str),
                primary_key=col_name in pk_set,
                nullable=nullable,
            )
        )
    return columns


def _parse_tables(sql_text: str) -> Dict[str, TableDefinition]:
    pk_map = _parse_primary_keys(sql_text)
    table_map: Dict[str, TableDefinition] = {}
    pattern = re.compile(
        r"CREATE TABLE public\.(?P<table>\w+)\s*\((?P<body>.*?)\);",
        re.DOTALL | re.IGNORECASE,
    )
    for match in pattern.finditer(sql_text):
        table = match.group("table")
        body = match.group("body")
        columns = _parse_columns(body, pk_map.get(table, []))
        table_map[table] = TableDefinition(name=table, columns=columns)
    return table_map


def _load_tables() -> Dict[str, Table]:
    sql_text = SQL_PATH.read_text(encoding="utf-8")
    definitions = _parse_tables(sql_text)
    tables: Dict[str, Table] = {}
    for name, definition in definitions.items():
        tables[name] = Table(name, _METADATA, *definition.columns)
    return tables


if SQL_PATH.exists():
    _TABLES = _load_tables()

TABLE_NAMES = sorted(_TABLES.keys())


def get_table(table_name: str) -> Table:
    if table_name not in _TABLES:
        raise KeyError(f"Unknown table: {table_name}")
    return _TABLES[table_name]


def create_tables() -> None:
    if _TABLES:
        _METADATA.create_all(bind=engine)
