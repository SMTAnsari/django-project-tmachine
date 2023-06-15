
from django.urls import path
from  .import views

urlpatterns = [
    path('', views.home),
    path('Home', views.index),
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('otp', views.OTP, name="otp"),
    path('email', views.email, name="email"),
    path('forget', views.forget, name="forget"),
]