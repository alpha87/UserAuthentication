"""
注册和登录表单
"""
from django import forms
from captcha.fields import CaptchaField


class LoginForm(forms.Form):
    """登录表单"""

    # 用户邮箱
    email = forms.EmailField()
    # 密码
    password = forms.CharField(widget=forms.PasswordInput())

    captcha = CaptchaField(label='验证码')


class RegistrationForm(forms.Form):
    """注册新用户表单"""

    # 邮箱
    email = forms.EmailField()
    # 用户名
    username = forms.CharField()
    # 密码
    password = forms.CharField(widget=forms.PasswordInput())
    # 二次输入密码
    password2 = forms.CharField(widget=forms.PasswordInput())


class RetakePassword(forms.Form):
    """修改密码"""

    # 密码
    password = forms.CharField(widget=forms.PasswordInput())
    # 二次输入密码
    password2 = forms.CharField(widget=forms.PasswordInput())
    # 验证码
    captcha = CaptchaField(label='验证码')


class Forgot(forms.Form):
    """忘记密码"""

    # 电子邮箱地址
    email = forms.EmailField()


class ForgotRetake(forms.Form):
    """验证邮箱后重新设置密码"""

    # email
    email = forms.EmailField()
    # 密码
    password = forms.CharField(widget=forms.PasswordInput())
    # 二次输入密码
    password2 = forms.CharField(widget=forms.PasswordInput())
    # 验证码
    captcha = CaptchaField(label='验证码')