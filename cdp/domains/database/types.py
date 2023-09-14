from dataclasses import (
    dataclass
)

DatabaseId = str


@dataclass
class Database:
    id: "DatabaseId"
    domain: str
    name: str
    version: str


@dataclass
class Error:
    message: str
    code: int


@dataclass
class ExecuteSQLReturnT:
    column_names: list
    values: list
    sql_error: "Error"


@dataclass
class GetDatabaseTableNamesReturnT:
    table_names: list
