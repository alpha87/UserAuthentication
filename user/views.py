from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.core.mail import send_mail

from .forms import LoginForm, RegistrationForm
from .models import User
from utils.send_email import send_email


"""
messages.debug(request, '%s SQL statements were executed.' % count)
messages.info(request, 'Three credits remain in your account.')
messages.success(request, 'Profile details updated.')
messages.warning(request, 'Your account expires in three days.')
messages.error(request, 'Document deleted.')
"""


def hello(request):
    """欢迎页面"""

    return render(request, "user/hello.html")


def logout(request):
    """登出用户"""

    if not request.session.get('is_login', None):
        return redirect("user:login")
    request.session.flush()
    return redirect("user:login")


def login(request):
    """登录用户"""

    if request.session.get('is_login', None):
        return redirect("user:hello")

    form = LoginForm(request.POST)

    if request.method == "POST":
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            try:
                user = User.objects.get(email=email)
            except:
                messages.warning(request, '用户不存在')
                return render(request, 'user/login.html', context={"form": form})
            if user.password_hash == password:
                request.session['is_login'] = True
                request.session['user_email'] = user.email
                request.session['user_name'] = user.username
                return redirect('user:hello')
            else:
                messages.warning(request, '密码错误')
                return render(request, 'user/login.html', context={"form": form})

    return render(request, "user/login.html", context={"form": form})


def sign_up(request):
    """注册新用户"""

    form = RegistrationForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            email = form.cleaned_data["email"]
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            password2 = form.cleaned_data["password2"]
            if password == password2:
                u = User(email=email, username=username,
                         password_hash=password)
                token = u.generate_token(email)
                link = request.build_absolute_uri(u.get_absolute_url(token))
                u.save()

                # 发送认证邮件
                send_email(receiver=email, link=link)
                messages.success(request, '注册成功，请及时查收确认邮件！')
                return redirect("user:login")
            else:
                messages.warning(request, '请检查两次输入密码是否一致！')
                return redirect("user:register")

    return render(request, "user/signup.html", context={"form": form})


def confirm(request, token):
    if not request.session.get('is_login', None):
        return redirect("user:login")
    email = request.session['user_email']
    user = User.objects.get(email=email)
    if user.confirmrd:
        messages.warning(request, '已经验证过！')
        return redirect("user:hello")
    else:
        if user.confirm(email=email, token=bytes(token, encoding="utf8")):
            user.confirmrd = True
            user.save()
            messages.success(request, '已验证')
            return redirect("user:hello")
        else:
            messages.warning(request, '认证失败')
            return redirect("user:hello")
