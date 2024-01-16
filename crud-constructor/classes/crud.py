from .table import Table
from mysqlclientpy import DB

class Crud:
    def __init__(
        self,
        tables: list[Table],
        client_sql: DB
    ) -> None:
        self.tables = tables
        self.client_sql = client_sql

        for table in self.tables:
            table.__set_client_sql__(self.client_sql)

    def __validate_tables__(self) -> None:
        for table in self.tables:
            table.create_table()