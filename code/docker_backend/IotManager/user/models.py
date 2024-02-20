from django.db import models

# Create your models here.

from django.db import models


class CustomUser(models.Model):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)

    # 如果需要保存加密后的密码，可以使用PasswordField
    # 否则，使用CharField，并在views中使用make_password保存密码
    password = models.CharField(max_length=128)

    def __str__(self):
        # 返回包含所有字段信息的字符串
        return f"User ID: {self.user_id}, Email: {self.email}, Username: {self.username}"
