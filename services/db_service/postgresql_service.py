# service/postgresql_service.py

import psycopg2

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from db_config import DB_CONFIG

class PostgreSQLService:
    def __init__(self):
        self.conn = None

    def _get_connection(self):
        if self.conn is None or self.conn.closed:
            try:
                self.conn = psycopg2.connect(**DB_CONFIG)
                print("Conexión a la base de datos PostgreSQL establecida.")
            except psycopg2.Error as e:
                print(f'Error al conectar a la base de datos PostgreSQL: {e}')
                self.conn = None # Asegurarse de que conn sea None en caso de error
        return self.conn

    def _close_connection(self):
        """Cierra la conexión a la base de datos PostgreSQL si está abierta."""
        if self.conn and not self.conn.closed:
            self.conn.close()
            self.conn = None
            print("Conexión a la base de datos PostgreSQL cerrada.")

    def obtener_producto_db_por_id(self, product_id):
        """
        Obtiene un producto de la base de datos PostgreSQL por su ID.
        """
        conn = self._get_connection()
        if not conn:
            return {"status": "error", "message": "No se pudo establecer la conexión a la base de datos."}
        
        try:
            with conn.cursor() as cursor:
                cursor.execute("SELECT id, nombre, descripcion, precio FROM productos WHERE id = %s", (product_id,))
                producto = cursor.fetchone()

                if producto:
                    # Mapea el resultado a un diccionario
                    columns = [desc[0] for desc in cursor.description]
                    return {"status": "success", "producto": dict(zip(columns, producto))}
                else:
                    return {"status": "error", "message": f"Producto con ID {product_id} no encontrado."}
        except psycopg2.Error as e:
            # Revertir cambios en caso de error
            conn.rollback()
            return {"status": "error", "message": f"Error al obtener el producto: {e}"}
        finally:
            # Opcionalmente cerrar la conexión
            #self._close_connection()
            pass

if __name__ == "__main__":
    db_service = PostgreSQLService()
    # Prueba obtener producto por ID
    prod_existente = db_service.obtener_producto_db_por_id("P001")
    print("\nResultado para P001:", prod_existente)

    # Prueba obtener producto por ID inexistente
    prod_inexistente = db_service.obtener_producto_db_por_id("P999")
    print("\nResultado para P999:", prod_inexistente)

    db_service._close_connection()  # Cerrar la conexión al final