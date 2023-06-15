
from django.urls import path
from  .import views

urlpatterns = [
    path('', views.home),
    path('Home', views.index),
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('otp', views.otp, name="otp"),
    path('forgot', views.forgot, name="forgot"),
    path('reset', views.reset, name="reset_password"),
]