



# FireBird
  
Conéctese a una base de datos Firebird; creá tablas; insertá o actualizá datos; realiza consultas personalizadas.  

  
*Read this in other languages: [English](Manual_FireBird.md), [Português](Manual_FireBird.pr.md), [Español](Manual_FireBird.es.md)*  

  
![banner](imgs/Banner_FireBird.jpg)
## Como instalar este módulo
  
Para instalar el módulo en Rocketbot Studio, se puede hacer de dos formas:
1. Manual: __Descargar__ el archivo .zip y descomprimirlo en la carpeta modules. El nombre de la carpeta debe ser el mismo al del módulo y dentro debe tener los siguientes archivos y carpetas: \__init__.py, package.json, docs, example y libs. Si tiene abierta la aplicación, refresca el navegador para poder utilizar el nuevo modulo.
2. Automática: Al ingresar a Rocketbot Studio sobre el margen derecho encontrara la sección de **Addons**, seleccionar **Install Mods**, buscar el modulo deseado y presionar install.  


## Descripción de los comandos

### Conectar
  
Conectarse a una base de datos de Firebird
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|DSN (Data Source Name)||[host[/port]]:database|
|Nombre de Usuario||ISC_USER|
|Contraseña||Valor Predeterminado ISC_PASSWORD|
|Sesión||Conn1|
|Asignar resultado a variable|Asignar resultado de la conexión a variable.|result|

### Consulta
  
Ejecutar una consulta personalizada.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Query||SELECT <column>, <column> FROM <table> WHERE <column> = <value> ...|
|Sesión||Conn1|
|Asignar resultado a variable|Asignar resultado de la conexión a variable.|result|

### Actualizar
  
Realiza modificaciones en una tabla de la base de datos.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Nombre de la tabla||Tabla|
|Nuevo valor por encabezado/columna||{header_1: value_1, header_2: value_2}|
|Condicionales||{header_3: condition}|
|Sesión||Conn1|
|Asignar resultado a variable|Asignar resultado de la conexión a variable.|result|

### Insertar
  
Insertar un registro a una tabla de la base de datos.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Nombre de la tabla||Tabla|
|Encabezados de la tabla||Nombre,Dirección|
|Valores a insertar||1, 'Will'|
|Sesión||Conn1|
|Asignar resultado a variable|Asignar resultado de la conexión a variable.|result|

### Crear Tabla
  
Crear una tabla dentro de la base de datos.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Nombre de la tabla||Tabla|
|Columna & Tipo de Dato||Nombre varchar(20),NumeroEmpleado int|
|Sesión||Conn1|
|Asignar resultado a variable|Asignar resultado de la conexión a variable.|result|

### Eliminar Tabla
  
Eliminar una tabla existente en la base de datos.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Nombre de la tabla||Tabla|
|Sesión||Conn1|
|Asignar resultado a variable|Asignar resultado de la conexión a variable.|result|

### Seleccionar Tabla
  
Recuperar los datos de una tabla completa de la base de datos.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Nombre de la tabla||Tabla|
|Sesión||Conn1|
|Asignar resultado a variable|Asignar resultado de la conexión a variable.|result|

### Cerra conexión
  
Cerrar la conexión a la base de datos.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Sesión||Conn1|
