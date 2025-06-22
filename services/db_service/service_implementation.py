# service_implementation.py
from microesb import microesb
from postgresql_service import PostgreSQLService

class Product(microesb.ClassHandler):
    def __init__(self):
        super().__init__()
        self.db_service = PostgreSQLService()

    def get_by_id(self):
        result = self.db_service.obtener_producto_db_por_id(self.id)
        print("Resultado de la consulta: ", result)
        return result
    
    def create(self):
        result = self.db_service.crear_producto(
            id=self.id,
            nombre=self.nombre,
            descripcion=self.descripcion,
            categoria=self.categoria,
            precio=self.precio
        )
        print("Resultado de la insercion: ", result)
        return result
    
    def update(self):
        # Se pasan solo los atributos que existen en self, lo que permite actualizaciones parciales
        update_data = {
            k: getattr(self, k) for k in ['nombre', 'descripcion', 'categoria', 'precio']
            if hasattr(self, k)
        }
        result = self.db_service.actualizar_producto(
            id=self.id,
            **update_data
        )
        print("Resultado de actualizacion: ", result)
        return result

    def delete(self):
        result = self.db_service.eliminar_producto(self.id)
        print("Resultado de la eliminacion: ", result)
        return result