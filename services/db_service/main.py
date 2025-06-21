# main.py
from microesb import microesb
from service_properties import service_properties
from class_reference import class_reference
from class_mapping import class_mapping
from service_call_metadata import service_metadata_create, service_metadata_delete, service_metadata_update

class_mapper = microesb.ClassMapper(
    class_references=class_reference,
    class_mappings=class_mapping,
    class_properties=service_properties
)

# --- PRUEBA 1: CREAR PRODUCTO ---
print("\n--- Probando CREAR PRODUCTO ---")
result_create = microesb.ServiceExecuter().execute(
    class_mapper=class_mapper,
    service_data=service_metadata_create
)
print(result_create)

# --- PRUEBA 2: OBTENER PRODUCTO RECIÉN CREADO ---
print("\n--- Probando OBTENER PRODUCTO CREADO (P005) ---")
# Modifica service_metadata para pedir P005
service_metadata_get_p005 = {
    'SYSServiceID': 'getProductById',
    'data': [
        {
            'Product': {
                'SYSServiceMethod': 'get_by_id',
                'id': 'P005'
            }
        }
    ]
}
result_get_p005 = microesb.ServiceExecuter().execute(
    class_mapper=class_mapper,
    service_data=service_metadata_get_p005
)
print(result_get_p005)

# --- PRUEBA 3: ACTUALIZAR PRODUCTO ---
print("\n--- Probando ACTUALIZAR PRODUCTO (P005) ---")
result_update = microesb.ServiceExecuter().execute(
    class_mapper=class_mapper,
    service_data=service_metadata_update
)
print(result_update)

# --- PRUEBA 4: OBTENER PRODUCTO ACTUALIZADO ---
print("\n--- Probando OBTENER PRODUCTO ACTUALIZADO (P005) ---")
result_get_updated_p005 = microesb.ServiceExecuter().execute(
    class_mapper=class_mapper,
    service_data=service_metadata_get_p005
)
print(result_get_updated_p005)

# --- PRUEBA 5: ELIMINAR PRODUCTO ---
print("\n--- Probando ELIMINAR PRODUCTO (P005) ---")
result_delete = microesb.ServiceExecuter().execute(
    class_mapper=class_mapper,
    service_data=service_metadata_delete
)
print(result_delete)

# --- PRUEBA 6: INTENTAR OBTENER PRODUCTO ELIMINADO ---
print("\n--- Probando OBTENER PRODUCTO ELIMINADO (P005) ---")
result_get_deleted_p005 = microesb.ServiceExecuter().execute(
    class_mapper=class_mapper,
    service_data=service_metadata_get_p005
)
print(result_get_deleted_p005)