from ..crud_constructor import Crud, Table, ColumnTypes, Column, RelationalColumn
from mysqlclientpy import DB

user_id_col = Column(
    name='id',
    default='UUID_TO_BIN(UUID())',
    type=ColumnTypes.BINARY,
    length=16,
    primary_key=True
)

users = Table(
    name='users',
    columns=[
        user_id_col,
        Column(
            name='name',
            type=ColumnTypes.VARCHAR,
            length=255
        ),
        Column(
            name='email',
            type=ColumnTypes.VARCHAR,
            length=255
        )
    ]
)

orders = Table(
    name='orders',
    columns=[
        Column(
            name='id',
            type=ColumnTypes.INTEGER,
            auto_increment=True,
            primary_key=True
        ),
        RelationalColumn(
            column=user_id_col,
            name='user_id',
            table_ref='users'
        ),
        Column(
            name='price',
            type=ColumnTypes.DECIMAL,
            length='10,2'
        )
    ]
)

crud = Crud(
    tables=[users],
    client_sql=DB(
        host='localhost',
        database='test',
        password='password',
        port=3306,
        user='root'
    )
)