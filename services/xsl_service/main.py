# main.py 
from microesb import microesb
# Asegúrate de que las importaciones apunten al nuevo directorio
from service_properties import service_properties
from class_reference import class_reference
from class_mapping import class_mapping

from service_call_metadata import service_metadata_xls_get_by_id, \
    service_metadata_xls_search_by_name, service_metadata_xls_list_all


class_mapper = microesb.ClassMapper(
    class_references=class_reference,
    class_mappings=class_mapping,
    class_properties=service_properties
)

# --- PRUEBA 1: OBTENER PRODUCTO DE XLS POR ID ---
print("\n--- Probando OBTENER PRODUCTO DE XLS POR ID (ID EL001) ---")
result_xls_get = microesb.ServiceExecuter().execute(
    class_mapper=class_mapper,
    service_data=service_metadata_xls_get_by_id
)
print(result_xls_get)

# --- PRUEBA 2: LISTAR TODOS LOS PRODUCTOS DE XLS ---
print("\n--- Probando LISTAR TODOS LOS PRODUCTOS DE XLS ---")
result_xls_list = microesb.ServiceExecuter().execute(
    class_mapper=class_mapper,
    service_data=service_metadata_xls_list_all
)
print(result_xls_list)

# --- PRUEBA 3: BUSCAR PRODUCTOS EN XLS POR NOMBRE ---
print("\n--- Probando BUSCAR PRODUCTOS EN XLS POR NOMBRE ('Cable') ---")
result_xls_search = microesb.ServiceExecuter().execute(
    class_mapper=class_mapper,
    service_data=service_metadata_xls_search_by_name
)
print(result_xls_search)