from django.db import models

from user.models import CustomUser


# Create your models here.
class Device(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='devices')
    device_id = models.CharField(max_length=100)
    device_name = models.CharField(max_length=255)
    device_location = models.CharField(max_length=255)
    device_type = models.CharField(max_length=100)
    device_status = models.CharField(max_length=10, choices=[('on', 'On'), ('off', 'Off')])
    is_online = models.BooleanField(default=False)  # 新添加的字段

    class Meta:
        unique_together = ('user', 'device_id')

    def __str__(self):
        return (f"Device(user_id={self.user.user_id}, device_id={self.device_id}, device_name={self.device_name}, "
                f"device_location={self.device_location}, device_type={self.device_type}, "
                f"device_status={self.device_status}, is_online={self.is_online})")
