
from django.urls import path
from  .import views

urlpatterns = [
    path('Home', views.index),
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
]