from enum import Enum

class ColumnTypes(Enum):
    """A sql column type enum"""
    INTEGER = 'INTEGER'
    TEXT = 'TEXT'
    BLOB = 'BLOB'
    DECIMAL = 'DECIMAL'
    FLOAT = 'FLOAT'
    BOOLEAN = 'BOOLEAN'
    DATE = 'DATE'
    DATETIME = 'DATETIME'
    TIME = 'TIME'
    TIMESTAMP = 'TIMESTAMP'
    JSON = 'JSON'
    VARCHAR = 'VARCHAR'