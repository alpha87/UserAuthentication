from django.db import models


class User(models.Model):
    """用户模型"""

    # 电子邮箱地址
    email = models.CharField(unique=True, max_length=200)
    # 用户昵称
    username = models.CharField(unique=True, max_length=200)
    # 哈希后的密码
    password_hash = models.CharField(unique=True, max_length=200)
    # 新增日期
    increase = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
