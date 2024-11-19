from django.urls import path
from django.views.decorators.cache import cache_page
from . import views



app_name = 'main'


urlpatterns = [
     path("",  views.TopSalesView.as_view(), name="main"),   
]