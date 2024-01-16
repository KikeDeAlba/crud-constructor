from ..enums.column_types import ColumnTypes

class Column:
    def __init__(
        self,
        name: str,
        type: ColumnTypes,
        default: str | None = None,
        primary_key=False
    ):
        self.name = name
        self.type = type
        self.primary_key = primary_key
        self.default = default

    def create_column_query(self) -> str:
        return f'{self.name} {self.type.value} {self.__primary_key__()} {self.__default__()}'

    def __primary_key__(self) -> str:
        return 'PRIMARY KEY' if self.primary_key else ''
    
    def __default__(self) -> str:
        return f'DEFAULT {self.default}' if self.default else ''
    
class RelationalColumn:
    def __init__(
        self,
        column: Column,
        name: str,
        on_delete: str | None = None,
        on_update: str | None = None,
        primary_key=False,
        default: str | None = None

    ) -> None:
        self.column = column
        self.name = name
        self.on_delete = on_delete
        self.on_update = on_update
        self.primary_key = primary_key
        self.default = default

    def create_column_query(self) -> str:
        return f'{self.name} {self.column.type.value} {self.__primary_key__()} {self.__default__()}'

    def __primary_key__(self) -> str:
        return 'PRIMARY KEY' if self.primary_key else ''
    
    def __default__(self) -> str:
        return f'DEFAULT {self.default}' if self.default else ''
    
    def set_table_name(self, table_name: str) -> None:
        self.table_name = table_name
    
    def __foreign_key__(self) -> str:
        return f'FOREIGN KEY ({self.name}) REFERENCES {self.table_name} ({self.column.name}) {self.__on_delete__()} {self.__on_update__()}'
    
    def __on_delete__(self) -> str:
        return f'ON DELETE {self.on_delete}' if self.on_delete else ''
    
    def __on_update__(self) -> str:
        return f'ON UPDATE {self.on_update}' if self.on_update else ''

    def create_foreign_key_query(self) -> str:
        return self.__foreign_key__()