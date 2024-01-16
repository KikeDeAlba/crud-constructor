from ..enums.column_types import ColumnTypes
from ..models.column_ref import ColumnRef

class Column:
    def __init__(
        self,
        name: str,
        type: ColumnTypes,
        default: str | None = None,
        primary_key=False,
        length: int | str | None = None,
        auto_increment: bool = False
    ):
        self.name = name
        self.type = type
        self.primary_key = primary_key
        self.default = default
        self.length = length
        self.auto_increment = auto_increment

    def create_column_query(self) -> str:
        return f'{self.name} {self.type.value}{self.__length__()} {self.__primary_key__()} {self.__auto_increment__()} {self.__default__()}'

    def __primary_key__(self) -> str:
        return 'PRIMARY KEY' if self.primary_key else ''
    
    def __length__(self) -> str:
        return f'({self.length})' if self.length else ''
    
    def __default__(self) -> str:
        return f'DEFAULT {self.default}' if self.default else ''
    
    def __auto_increment__(self) -> str:
        return 'AUTO_INCREMENT' if self.auto_increment else ''
    
class RelationalColumn:
    def __init__(
        self,
        column: ColumnRef,
        name: str,
        on_delete: str | None = None,
        on_update: str | None = None,
        primary_key=False,
        default: str | None = None,
    ) -> None:
        self.column_ref = column
        self.name = name
        self.on_delete = on_delete
        self.on_update = on_update
        self.primary_key = primary_key
        self.default = default
        self.auto_increment = False

    def create_column_query(self) -> str:
        return f'{self.name} {self.column_ref.column.type.value}{self.__length__()} {self.__primary_key__()} {self.__default__()}'

    def __primary_key__(self) -> str:
        return 'PRIMARY KEY' if self.primary_key else ''
    
    def __default__(self) -> str:
        return f'DEFAULT {self.default}' if self.default else ''
    
    def __foreign_key__(self) -> str:
        return f'FOREIGN KEY ({self.name}) REFERENCES {self.column_ref.table} ({self.column_ref.column.name}) {self.__on_delete__()} {self.__on_update__()}'
    
    def __on_delete__(self) -> str:
        return f'ON DELETE {self.on_delete}' if self.on_delete else ''
    
    def __on_update__(self) -> str:
        return f'ON UPDATE {self.on_update}' if self.on_update else ''
    
    def __length__(self) -> str:
        return f'({self.column_ref.column.length})' if self.column_ref.column.length else ''

    def create_foreign_key_query(self) -> str:
        return self.__foreign_key__()