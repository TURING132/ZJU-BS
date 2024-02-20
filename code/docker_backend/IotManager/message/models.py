from django.db import models
from device.models import Device


class Message(models.Model):
    MESSAGE_TYPES = [
        ('normal', 'Normal'),
        ('location', 'Location'),
        ('warning', 'Warning'),
    ]
    id = models.AutoField(primary_key=True)
    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name='messages')
    type = models.CharField(max_length=10, choices=MESSAGE_TYPES, default='normal')
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f"Message(id={self.id}, type={self.type}), device_id={self.device.device_id}, text={self.text}, "
                f"timestamp={self.timestamp}")
