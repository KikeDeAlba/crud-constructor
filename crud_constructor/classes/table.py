from .column import Column, RelationalColumn
from mysqlclientpy import DB

class Table:
    def __init__(
        self,
        name: str,
        columns: list[Column | RelationalColumn],
    ) -> None:
        self.name = name
        self.columns = columns

    def __set_client_sql__(self, client: DB) -> None:
        self.client_sql = client

    def __create_table_query__(self) -> str:
        columns = ', '.join([column.create_column_query() for column in self.columns])
        return f'CREATE TABLE IF NOT EXISTS {self.name} ({columns})'
    
    def create_table(self) -> None:
        table_sql = self.__create_table_query__()

        for column in self.columns:
            if isinstance(column, RelationalColumn):
                ref = column.create_foreign_key_query()

                table_sql += f', {ref}'

        self.client_sql.execute(table_sql)
        self.__validate_columns_exists_in_db__()

    def __validate_columns_exists_in_db__(self) -> None:
        for column in self.columns:
            column_exist = self.client_sql.fetch_one(f'SHOW COLUMNS FROM {self.name} WHERE Field = "{column.name}"')
            
            if not column_exist:
                self.client_sql.execute(f'ALTER TABLE {self.name} ADD {column.create_column_query()}')