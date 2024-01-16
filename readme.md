# CRUD Constructor

## Descripción
Esta es una librería en desarrollo llamada `crud-constructor` que proporciona herramientas para simplificar la creación y gestión de operaciones CRUD (Crear, Leer, Actualizar, Eliminar) en bases de datos MySQL utilizando Python.

## Clases Principales

### `Crud`
La clase principal `Crud` es responsable de gestionar las operaciones CRUD para un conjunto de tablas. Al instanciar un objeto `Crud`, se deben proporcionar las tablas y el cliente MySQL correspondiente. La inicialización realiza la validación de las tablas y crea las tablas si no existen.

Ejemplo de uso:
```python
from crud_constructor import Crud, Table
from mysqlclientpy import DB

# Definir las tablas
table1 = Table(name="users", columns=[...])
table2 = Table(name="products", columns=[...])

# Crear el objeto Crud
crud = Crud(tables=[table1, table2], client_sql=DB(...))
```

### `Table`
La clase `Table` representa una tabla en la base de datos y define sus columnas. Cada tabla se asocia con un objeto `DB` que actúa como el cliente SQL.

Ejemplo de uso:
```python
from crud_constructor import Table, Column, RelationalColumn
from ..enums.column_types import ColumnTypes

# Definir columnas para la tabla
column1 = Column(name="id", type=ColumnTypes.INT, primary_key=True)
column2 = Column(name="name", type=ColumnTypes.VARCHAR, default="'Unknown'")
relational_column = RelationalColumn(column=column1, name="user_id", on_delete="CASCADE")

# Crear la tabla
users_table = Table(name="users", columns=[column1, column2, relational_column])
```

### `Column` y `RelationalColumn`
Estas clases definen columnas simples y columnas relacionales, respectivamente. Puedes crear columnas con diferentes tipos de datos y especificar restricciones como claves primarias, valores predeterminados y claves foráneas.

## Uso
1. Instala la librería utilizando pip:
   ```bash
   pip install crud-constructor
   ```

2. Importa las clases necesarias y crea instancias de `Crud`, `Table`, `Column`, y `RelationalColumn`.

3. Define las tablas y columnas que deseas utilizar en tu base de datos.

4. Crea un objeto `Crud` con las tablas y el cliente MySQL.

5. ¡Estás listo para realizar operaciones CRUD en tu base de datos!

## Notas
- Este proyecto está en desarrollo y se agregarán nuevas características.
- La generación de HTML para el CRUD es una característica planificada (ver `__html__` en `Crud`).
- Asegúrate de tener el paquete `mysqlclientpy` instalado y configurado correctamente.

¡Gracias por usar `crud-constructor`! Si encuentras algún problema o tienes sugerencias, no dudes en abrir un issue en el repositorio. ¡Contribuciones son bienvenidas!