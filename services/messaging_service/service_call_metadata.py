service_metadata_send_purchase = {
    'SYSServiceID': 'sendPurchaseNotificacion', 
    'data': [
        {
            'MessagingService': {
                'SYSServiceMethod': 'send_purchase_notification',
                'compra_data': {
                    "order_id": "ORD002",
                    "product_id": "P003",
                    "quantity": 1,
                    "customer_email": "otro@example.com",
                    "timestamp": "2025-06-21T10:30:00Z"
                }
            }
        }
    ]
}

service_metadata_register_log = {
    'SYSServiceID': 'registerLogEvent',
    'data': [
        {
            'MessagingService': {
                'SYSServiceMethod': 'register_log_event',
                'log_data': {
                    "level": "WARNING",
                    "message": "Intento de acceso fallido desde IP 192.168.1.10.",
                    "service": "security",
                    "timestamp": "2025-06-21T10:35:00Z"
                }
            }
        }
    ]
}