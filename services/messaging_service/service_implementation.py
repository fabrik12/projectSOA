# messaging_service/messaging_service.py

from microesb import microesb
from rabbitmq_service import RabbitMQService # Importar implementacion del servicio

class MessagingService(microesb.ClassHandler):
    def __init__(self):
        super().__init__()
        self.mq_service = RabbitMQService()

    def send_purchase_notification(self):
        # self.compra_data es inyectado por el ESB
        return self.mq_service.enviar_notificacion_compra(self.compra_data)
    
    def register_log_event(self):
        # self.log_data es inyectado por el ESB
        return self.mq_service.registrar_evento_log(self.log_data)