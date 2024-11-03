from django.urls import path

from . import views



app_name = 'users'


urlpatterns = [
     path("login/", views.login, name="login"),
     path("reqistration/", views.registration, name="registration"),
     path("logout/", views.logout, name="logout"),  
     path("users-cart/", views.user_cart, name="cart"),
     ]