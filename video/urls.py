
from django.urls import path
from  .import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home),
    path('Home', views.index),
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('otp/<str:email>/', views.otp, name='otp'),
    path('otpForgot/<str:email>/', views.otpForgot, name='otpForgot'),
    path('forgot', views.forgot, name="forgot"),
    path('reset/<str:email>/', views.reset, name="reset"),
 
]