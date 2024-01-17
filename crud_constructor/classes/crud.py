from .table import Table
from mysqlclientpy import DB
from dotenv import load_dotenv
from mysqlclientpy import DB
import os
load_dotenv()

class Crud:
    def __init__(
        self,
        tables: list[Table],
        host: str | None = None,
        database: str | None = None,
        password: str | None = None,
        port: int | str | None = None,
        user: str | None = None
    ) -> None:
        self.tables = tables

        host = host or os.environ.get('DB_HOST')
        database = database or os.environ.get('DB_DATABASE')
        password = password or os.environ.get('DB_PASSWORD')
        port = port or os.environ.get('DB_PORT') or 3306
        user = user or os.environ.get('DB_USER')

        if not host or not database or not password or not port or not user:
            raise Exception('You must provide the database connection parameters')

        self.client_sql = DB(
            host=host,
            database=database,
            password=password,
            port=int(port),
            user=user
        )

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