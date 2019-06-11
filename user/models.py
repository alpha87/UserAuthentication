from django.db import models
from django.conf import settings
from itsdangerous import TimedJSONWebSignatureSerializer as ser
from django.shortcuts import reverse

import datetime


class User(models.Model):
    """用户模型"""

    # 用户ID
    _id = models.IntegerField(auto_created=True, primary_key=True)
    # 电子邮箱地址
    email = models.CharField(unique=True, max_length=200)
    # 用户昵称
    username = models.CharField(unique=True, max_length=200)
    # 哈希后的密码
    password_hash = models.CharField(max_length=200)
    # 新增日期
    increase = models.DateTimeField(auto_now_add=True)
    # token
    confirmrd = models.BooleanField(default=False)

    def generate_token(self, email, expiration=3600):
        s = ser(secret_key=settings.SECRET_KEY, expires_in=expiration)
        token = str(s.dumps({"confirm": email}), encoding="utf8")
        return token

    def confirm(self, email, token):
        s = ser(secret_key=settings.SECRET_KEY)
        try:
            data = s.loads(token)
        except :
            return False
        if data.get("confirm") != email:
            return False
        self.confirmed = True
        self.save()
        return True

    def get_absolute_url(self, token):
        return reverse("user:confirm", args=[token])

    def get_forgot_absolute_url(self, token):
        return reverse("user:forgot_confirm", args=[token])

    def __str__(self):
        return self.username
