from django.urls import path

from . import views



app_name = 'main'


urlpatterns = [
     path("", views.top_sales, name="main"),   
]