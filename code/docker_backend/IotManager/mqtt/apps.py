from django.apps import AppConfig


class MqttConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mqtt'


    def ready(self):
        from mqtt.utils import connect_to_mqtt
        self.received_bytes = 0
        self.sent_bytes = 0
        self.client = connect_to_mqtt()
        self.client.loop_start()