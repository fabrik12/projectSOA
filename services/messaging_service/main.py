from microesb import microesb
from service_properties import service_properties
from class_reference import class_reference
from class_mapping import class_mapping

# Nuevos metadatos de llamada para mensajería
from service_call_metadata import service_metadata_register_log, service_metadata_send_purchase


class_mapper = microesb.ClassMapper(
    class_references=class_reference,
    class_mappings=class_mapping,
    class_properties=service_properties
)

# --- PRUEBA 1: ENVIAR NOTIFICACIÓN DE COMPRA ---
print("\n--- Probando ENVIAR NOTIFICACIÓN DE COMPRA ---")
result_send_purchase = microesb.ServiceExecuter().execute(
    class_mapper=class_mapper,
    service_data=service_metadata_send_purchase
)
print(result_send_purchase)

# --- PRUEBA 2: REGISTRAR EVENTO DE LOG ---
print("\n--- Probando REGISTRAR EVENTO DE LOG ---")
result_register_log = microesb.ServiceExecuter().execute(
    class_mapper=class_mapper,
    service_data=service_metadata_register_log
)
print(result_register_log)