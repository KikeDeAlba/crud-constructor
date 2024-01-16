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

        self.__validate_tables__()

    def __validate_tables__(self) -> None:
        for table in self.tables:
            table.create_table()

    #TODO: Implementar o método __html__ para gerar o html do crud
    # def __html__(self) -> str:
    #     html = '''
            
    #     '''

    #     for table in self.tables:
    #         html += table.__html__()