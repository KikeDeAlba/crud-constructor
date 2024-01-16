from pydantic import BaseModel
from ..classes.column import Column

class ColumnRef(BaseModel):
    column: Column
    table: str