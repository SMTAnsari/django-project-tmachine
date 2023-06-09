
from django.urls import path
from  .import views

urlpatterns = [
    path('Home', views.index),
    path('', views.login, name="login"),
    path('register', views.register, name="register"),
]