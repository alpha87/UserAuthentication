from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import LoginForm, RegistrationForm
from .models import User


"""
messages.debug(request, '%s SQL statements were executed.' % count)
messages.info(request, 'Three credits remain in your account.')
messages.success(request, 'Profile details updated.')
messages.warning(request, 'Your account expires in three days.')
messages.error(request, 'Document deleted.')
"""


def hello(request):

    return render(request, "user/hello.html")


def logout(request):

    if not request.session.get('is_login', None):
        return redirect("user:login")
    request.session.flush()
    return redirect("user:login")


def login(request):

    if request.session.get('is_login', None):
        return redirect("user:hello")

    form = LoginForm(request.POST)

    if request.method == "POST":

        print(request.POST)

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
                request.session['user_id'] = user.email
                request.session['user_name'] = user.username
                return redirect('user:hello')
            else:
                messages.warning(request, '密码错误')
                return render(request, 'user/login.html', context={"form": form})

    return render(request, "user/login.html", context={"form": form})


def sign_up(request):

    form = RegistrationForm(request.POST)
    print("[ SIGN UP ]")
    if request.method == "POST":
        print(form.is_valid())
        if form.is_valid():
            email = form.cleaned_data["email"]
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            password2 = form.cleaned_data["password2"]

            if password == password2:
                u = User(email=email, username=username,
                         password_hash=password)
                u.save()
                messages.success(request, '注册成功，请及时查收确认邮件！')
                return redirect("user:login")
            else:
                messages.warning(request, '请检查两次输入密码是否一致！')
                return redirect("user:register")

    return render(request, "user/signup.html", context={"form": form})
