# service_properties.py
service_properties = {
    'MessagingService': { # Nueva entrada para el servicio de mensajería
        'properties': {
            'compra_data': {'type': 'dict', 'required': False, 'default': None}, # Para send_purchase_notification
            'log_data': {'type': 'dict', 'required': False, 'default': None}     # Para register_log_event
        },
        'methods': ['send_purchase_notification', 'register_log_event']
    }
}