from ..crud_constructor import Crud, Table, ColumnTypes, Column, RelationalColumn

users_table = Table(
    name='users',
    columns=[
        Column(
            name='id',
            default='UUID_TO_BIN(UUID())',
            type=ColumnTypes.BINARY,
            length=16,
            primary_key=True
        ),
        Column(
            name='name',
            type=ColumnTypes.VARCHAR,
        ),
        Column(
            name='email',
            type=ColumnTypes.VARCHAR,
        )
    ]
)

orders_table = Table(
    name='orders',
    columns=[
        Column(
            name='id',
            type=ColumnTypes.INTEGER,
            auto_increment=True,
            primary_key=True
        ),
        RelationalColumn(
            column=users_table.get_column('id'),
            name='user_id'
        ),
        Column(
            name='price',
            type=ColumnTypes.DECIMAL,
            length='10,2'
        )
    ]
)

crud = Crud(
    tables=[users_table],
    host='localhost',
    database='test',
    password='password',
    port=3306,
    user='root'
)