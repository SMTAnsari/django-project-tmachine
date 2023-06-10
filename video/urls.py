
from django.urls import path
from  .import views

urlpatterns = [
    path('', views.home),
    path('Home', views.index),
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
]