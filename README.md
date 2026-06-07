# Sistema de Gestión de Inventario con MCP y SQLite

## Descripción

Este proyecto implementa un servidor MCP (Model Context Protocol) para la administración de un inventario de productos utilizando SQLite como sistema de almacenamiento de datos y FastMCP como framework para la exposición de herramientas.

El sistema permite realizar operaciones CRUD (Crear, Consultar, Actualizar y Eliminar) sobre productos almacenados en una base de datos local, además de ejecutar consultas analíticas sobre el inventario.

## Funcionalidades

### Gestión de productos

* Crear productos
* Consultar productos por ID
* Listar productos registrados
* Actualizar cantidades de inventario
* Eliminar productos

### Consultas analíticas

* Calcular valor total del inventario
* Identificar productos agotados
* Consultar el producto más costoso
* Obtener estadísticas generales del inventario

## Tecnologías utilizadas

* Python 3.x
* SQLite
* FastMCP
* Visual Studio Code

## Estructura del proyecto

mcp_inventory/

├── server.py

├── database.py

├── inventory.db

├── requirements.txt

└── README.md

## Instalación

### Clonar repositorio

git clone [https://github.com/USUARIO/mcp-inventory-system.git](https://github.com/javieralejandro9522-sudo/mcp-inventory-system.git)

cd mcp-inventory-system

### Crear entorno virtual

python -m venv venv

### Activar entorno virtual

Windows:

venv\Scripts\activate

### Instalar dependencias

pip install -r requirements.txt

## Ejecución

Ejecutar el servidor:

python server.py

## Pruebas realizadas

Se realizaron pruebas de:

* Creación de productos
* Consulta de productos
* Actualización de inventario
* Eliminación de registros
* Listado de productos
* Cálculo del valor total del inventario
* Identificación de productos agotados
* Consulta del producto más costoso
* Generación de estadísticas generales

## Autor

Alejandro Rodríguez y Milena Lizcano

Curso: Computación Cognitiva para Big Data
