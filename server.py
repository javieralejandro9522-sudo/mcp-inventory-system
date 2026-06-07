import sqlite3
from mcp.server.fastmcp import FastMCP
from database import init_db, DB_NAME

# Inicializar la base de datos al arrancar el servidor
init_db()

# Crear la instancia de FastMCP
mcp = FastMCP("InventarioDB")

def get_connection():
    return sqlite3.connect(DB_NAME)

# ==========================================
# PARTE 2: OPERACIONES CRUD
# ==========================================

@mcp.tool()
def crear_producto(nombre: str, categoria: str, cantidad: int, precio: float) -> str:
    """Crea un nuevo producto en el inventario."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO productos (nombre, categoria, cantidad, precio) VALUES (?, ?, ?, ?)",
        (nombre, categoria, cantidad, precio)
    )
    conn.commit()
    conn.close()
    return "Producto creado exitosamente"

@mcp.tool()
def consultar_producto(id: int) -> dict:
    """Consulta un producto específico por su ID."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre, categoria, cantidad, precio FROM productos WHERE id = ?", (id,))
    row = cursor.fetchone()
    conn.close()
    
    if row:
        return {
            "id": row[0],
            "nombre": row[1],
            "categoria": row[2],
            "cantidad": row[3],
            "precio": row[4]
        }
    return {"error": "Producto no encontrado"}

@mcp.tool()
def actualizar_producto(id: int, cantidad: int) -> str:
    """Actualiza la cantidad en stock de un producto por su ID."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE productos SET cantidad = ? WHERE id = ?",
        (cantidad, id)
    )
    conn.commit()
    conn.close()
    return "Producto actualizado correctamente"

@mcp.tool()
def eliminar_producto(id: int) -> str:
    """Elimina un producto del inventario mediante su ID."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM productos WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return "Producto eliminado correctamente"

@mcp.tool()
def listar_productos() -> list:
    """Devuelve la lista completa de productos en el inventario."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre, categoria, cantidad, precio FROM productos")
    rows = cursor.fetchall()
    conn.close()
    
    return [
        {
            "id": row[0],
            "nombre": row[1],
            "categoria": row[2],
            "cantidad": row[3],
            "precio": row[4]
        }
        for row in rows
    ]

# ==========================================
# PARTE 3: HERRAMIENTAS ANALÍTICAS
# ==========================================

@mcp.tool()
def calcular_valor_total_inventario() -> dict:
    """Calcula el valor económico total de todo el inventario (cantidad * precio)."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(cantidad * precio) FROM productos")
    total = cursor.fetchone()[0]
    conn.close()
    return {"valor_total_inventario": total if total else 0}

@mcp.tool()
def productos_agotados() -> list:
    """Devuelve una lista de los productos que tienen stock igual a 0."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre, categoria, cantidad, precio FROM productos WHERE cantidad = 0")
    rows = cursor.fetchall()
    conn.close()
    
    return [
        {
            "id": row[0],
            "nombre": row[1],
            "categoria": row[2],
            "cantidad": row[3],
            "precio": row[4]
        }
        for row in rows
    ]

@mcp.tool()
def producto_mas_costoso() -> dict:
    """Identifica el producto con el precio unitario más alto."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre, categoria, cantidad, precio FROM productos ORDER BY precio DESC LIMIT 1")
    row = cursor.fetchone()
    conn.close()
    
    if row:
        return {
            "id": row[0],
            "nombre": row[1],
            "categoria": row[2],
            "cantidad": row[3],
            "precio": row[4]
        }
    return {"error": "No hay productos registrados"}

@mcp.tool()
def estadisticas_inventario() -> dict:
    """Obtiene estadísticas generales: total de productos, promedios y valor total."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*), AVG(cantidad), AVG(precio), SUM(cantidad * precio) FROM productos")
    total_productos, promedio_cantidad, promedio_precio, valor_total = cursor.fetchone()
    conn.close()
    
    return {
        "total_productos": total_productos,
        "promedio_cantidad": promedio_cantidad if promedio_cantidad else 0,
        "promedio_precio": promedio_precio if promedio_precio else 0,
        "valor_total": valor_total if valor_total else 0
    }

if __name__ == "__main__":

    print(crear_producto(
        "Laptop HP",
        "Tecnología",
        10,
        2500000
    ))

    print(crear_producto(
        "Mouse Logitech",
        "Accesorios",
        20,
        80000
    ))

    print(crear_producto(
        "Monitor Samsung",
        "Tecnología",
        5,
        950000
    ))

    print(crear_producto(
        "Teclado",
        "Accesorios",
        15,
        180000
    ))

    print(crear_producto(
        "Disco SSD",
        "Almacenamiento",
        12,
        300000
    ))
print(listar_productos())

print(consultar_producto(5))

print(actualizar_producto(1,15))

print(consultar_producto(1))

print(eliminar_producto(2))

print(listar_productos())

print(calcular_valor_total_inventario())

print(producto_mas_costoso())

print(estadisticas_inventario())