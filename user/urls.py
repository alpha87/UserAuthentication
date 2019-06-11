from django.urls import path
from . import views


app_name="user"

urlpatterns = [
    path('', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('hello/', views.hello, name='hello'),
    path('register/', views.sign_up, name='register'),
    path('confirm/<token>', views.confirm, name='confirm'),
    path('forgot_confirm/<token>', views.forgot_confirm, name='forgot_confirm'),
    path('retake-password/', views.retake_password, name='retake-password'),
    path('forgot/', views.forgot, name='forgot')
]