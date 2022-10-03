from django.urls import path
from . import views


urlpatterns = [
    path('login', views.LoginView, name="login" ),
    path('signup', views.SignupView, name="signup")
]