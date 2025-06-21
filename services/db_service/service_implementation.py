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