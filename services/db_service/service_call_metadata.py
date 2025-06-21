# service_call_metadata.py
service_metadata = {
    'SYSServiceID': 'getProductById',
    'data': [
        {
            'Product': {
                'SYSServiceMethod': 'get_by_id',
                'id': 'P001'
            }
        }
    ]
}

service_metadata_create = {
    'SYSServiceID': 'createProduct',
    'data': [
        {
            'Product': {
                'SYSServiceMethod': 'create',
                'id': 'P005',
                'nombre': 'Auriculares Bluetooth',
                'descripcion': 'Auriculares inalámbricos con cancelación de ruido',
                'categoria': 'Audio',
                'precio': 99.99
            }
        }
    ]
}

service_metadata_update = {
    'SYSServiceID': 'updateProductById',
    'data': [
        {
            'Product': {
                'SYSServiceMethod': 'update',
                'id': 'P005',
                'precio': 109.99, # Solo actualizamos el precio
                'descripcion': 'Auriculares inalámbricos con sonido HD' # Y la descripción
            }
        }
    ]
}

service_metadata_delete = {
    'SYSServiceID': 'deleteProductById',
    'data': [
        {
            'Product': {
                'SYSServiceMethod': 'delete',
                'id': 'P005'
            }
        }
    ]
}