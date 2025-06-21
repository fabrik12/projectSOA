# service_properties.py
service_properties = {
    'Product': {
        'properties': {
            'id': {'type': 'string', 'required': True, 'default': None},
            'nombre': {'type': 'string', 'required': False, 'default': None}, # Ahora puede ser opcional para update
            'descripcion': {'type': 'string', 'required': False, 'default': None},
            'categoria': {'type': 'string', 'required': False, 'default': None},
            'precio': {'type': 'float', 'required': False, 'default': None} # Usamos float aquí para la entrada, aunque internamente use Decimal
        },
        'methods': ['get_by_id', 'create', 'update', 'delete'] # Añadimos los nuevos métodos CRUD
    }
}