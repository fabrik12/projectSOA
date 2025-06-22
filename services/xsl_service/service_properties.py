service_properties = {
    'ExcelCatalogoHandler': {
        'properties': {
            'product_id': {'type': 'string', 'required': False, 'default': None}, # Para get_by_id
            'nombre_parcial': {'type': 'string', 'required': False, 'default': None} # Para search_by_name
        },
        'methods': ['get_by_id', 'list_all', 'search_by_name']
    }
}