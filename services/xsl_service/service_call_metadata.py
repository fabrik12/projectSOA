# xsl_service/xsl_service.py

service_metadata_xls_get_by_id = {
    'SYSServiceID': 'getById',
    'data': [
        {
            'ExcelCatalogoHandler': {
                'SYSServiceMethod': 'get_by_id',
                'product_id': 'EL001' 
            }
        }
    ]
}

service_metadata_xls_list_all = {
    'SYSServiceID': 'listAll',
    'data': [
        {
            'ExcelCatalogoHandler': {
                'SYSServiceMethod': 'list_all_products'
                # No se necesitan datos adicionales
            }
        }
    ]
}

service_metadata_xls_search_by_name = {
    'SYSServiceID': 'searchByName',
    'data': [
        {
            'ExcelCatalogoHandler': {
                'SYSServiceMethod': 'search_products_by_name',
                'nombre_parcial': 'Cable'
            }
        }
    ]
}